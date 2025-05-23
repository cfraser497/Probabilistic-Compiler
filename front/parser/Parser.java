package parser;
import java.io.*; import lexer.*; import symbols.*; import inter.*; 
import java.util.List;
import java.util.Map;
import java.util.Properties;
import java.util.ArrayList;
import java.util.LinkedHashMap;

public class Parser {

   private Lexer lex;    // lexical analyzer for this parser
   private Token look;   // lookahead tagen
   Env top = null;       // current or top symbol table
   int used = 0;         // storage used for declarations
   
   int minInt;
   int maxInt;
   Map<String, Id> declaredVariables = new LinkedHashMap<>();


   public Parser(Lexer l, Properties props) throws IOException { 
      this.minInt = Integer.parseInt(props.getProperty("minInt"));
      this.maxInt = Integer.parseInt(props.getProperty("maxInt"));
      
      lex = l; move(); 
   }

   void move() throws IOException { look = lex.scan(); }

   void error(String s) { throw new Error("near line "+lex.line+": "+s); }

   void match(int t) throws IOException {
      if( look.tag == t ) move();
      else error("Unexpected Token:" + look);
   }

   public void program() throws IOException {  // program -> block
      Stmt s = block(); emitdata();
      int begin = s.newlabel();  int after = s.newlabel();
      System.out.println(".code:");
      s.emitlabel(begin);  s.gen(begin, after);  s.emitstoplabel(after);
   }

   Stmt block() throws IOException {  // block -> { decls stmts }
      match('{');  Env savedEnv = top;  top = new Env(top);
      decls(); Stmt s = stmts();
      match('}');  top = savedEnv;
      return s;
   }

   void decls() throws IOException {
      while (look.tag == Tag.BASIC) {
          TypeInfo typed = type();
          Token tok = look;
          match(Tag.ID);
          match(';');
  
          Id id;
          if (typed.range != null) {
              id = new Id((Word) tok, typed.type, used, typed.range);
          } else {
              id = new Id((Word) tok, typed.type, used);
          }
  
          top.put(tok, id);
  
          // Only add to declaredVariables if first declaration
          String varName = tok.toString();
          if (!declaredVariables.containsKey(varName)) {
              declaredVariables.put(varName, id);
          }
  
          used += typed.type.width;
      }
  }

   TypeInfo type() throws IOException {
      Word word = (Word) look;
      match(Tag.BASIC);
  
      Type base;
      switch (word.lexeme) {
          case "int": base = Type.Int; break;
          case "float": base = Type.Float; break;
          case "char": base = Type.Char; break;
          case "bool": base = Type.Bool; break;
          default: error("Unknown type"); return null;
      }
  
      Range range = null;
  
      if (base == Type.Int) {
          if (look.tag == '{') {
              match('{');
              if (look.tag != Tag.NUM) error("Expected number");
              int first = ((Num) look).value;
              move();
  
              if (look.tag == Tag.SPREAD) {
                  match(Tag.SPREAD);
                  if (look.tag != Tag.NUM) error("Expected number after '..'");
                  int last = ((Num) look).value;
                  move();
                  match('}');
                  range = new Range(base, first, last);
              } else {
                  List<Integer> values = new ArrayList<>();
                  values.add(first);
                  while (look.tag == ',') {
                      match(',');
                      if (look.tag != Tag.NUM) error("Expected number");
                      values.add(((Num) look).value);
                      move();
                  }
                  match('}');
                  if (values.size() > 256) error("Too many values");
                  range = new Range(base, values);
              }
          } else {
              range = new Range(base, minInt, maxInt);
          }
      }
  
      if (look.tag == '[') {
          base = dims(base);
      }
  
      return new TypeInfo(base, range);
   }


   Type dims(Type p) throws IOException {
      match('[');  Token tok = look;  match(Tag.NUM);  match(']');
      if( look.tag == '[' )
      p = dims(p);
      return new Array(((Num)tok).value, p);
   }

   Stmt stmts() throws IOException {
      if ( look.tag == '}' ) return Stmt.Null;
      else return new Seq(stmt(), stmts());
   }

   Stmt stmt() throws IOException {
      Expr x;  Stmt s, s1, s2;
      Stmt savedStmt;         // save enclosing loop for breaks

      switch( look.tag ) {

      case ';':
         move();
         return Stmt.Null;

      case Tag.IF:
         match(Tag.IF); match('('); x = bool(); match(')');
         s1 = stmt();
         if( look.tag != Tag.ELSE ) return new If(x, s1);
         match(Tag.ELSE);
         s2 = stmt();
         return new Else(x, s1, s2);

      case Tag.WHILE:
         While whilenode = new While();
         savedStmt = Stmt.Enclosing; Stmt.Enclosing = whilenode;
         match(Tag.WHILE); match('('); x = bool(); match(')');
         s1 = stmt();
         whilenode.init(x, s1);
         Stmt.Enclosing = savedStmt;  // reset Stmt.Enclosing
         return whilenode;

      case Tag.DO:
         Do donode = new Do();
         savedStmt = Stmt.Enclosing; Stmt.Enclosing = donode;
         match(Tag.DO);
         s1 = stmt();
         match(Tag.WHILE); match('('); x = bool(); match(')'); match(';');
         donode.init(s1, x);
         Stmt.Enclosing = savedStmt;  // reset Stmt.Enclosing
         return donode;

      case Tag.BREAK:
         match(Tag.BREAK); match(';');
         return new Break();

      // choose statement
      case Tag.CHOOSE:
         match(Tag.CHOOSE); match('{');

         List<Branch> branches = new ArrayList<>();
         int totalWeight = 0;

         while(look.tag != '}') {
            if(look.tag != Tag.NUM) {
               error("Expected a numeric branch label in choose statement");
            }

            int value = ((Num) look).value;
            move(); match(':');
            Stmt stmt = stmt();
            totalWeight += value;
            branches.add(new Branch(value, stmt));
         }
         match('}');
         return new Choose(branches, totalWeight);

      // stop stmt
      case Tag.STOP:
         match(Tag.STOP); match(';');
         return new Stop();

      case '{':
         return block();

      default:
         return assign();
      }
   }

   Stmt assign() throws IOException {
      Stmt stmt;  Token t = look;
      match(Tag.ID);
      Id id = top.get(t);
      if( id == null ) error(t.toString() + " undeclared");

      if( look.tag == '=' ) {       // S -> id = E ;
         move();  stmt = new Set(id, bool());
      }
      else {                        // S -> L = E ;
         Access x = offset(id);
         match('=');  stmt = new SetElem(x, bool());
      }
      match(';');
      return stmt;
   }

   Expr bool() throws IOException {
      Expr x = join();
      while( look.tag == Tag.OR ) {
         Token tok = look;  move();  x = new Or(tok, x, join());
      }
      return x;
   }

   Expr join() throws IOException {
      Expr x = equality();
      while( look.tag == Tag.AND ) {
         Token tok = look;  move();  x = new And(tok, x, equality());
      }
      return x;
   }

   Expr equality() throws IOException {
      Expr x = rel();
      while( look.tag == Tag.EQ || look.tag == Tag.NE ) {
         Token tok = look;  move();  x = new Rel(tok, x, rel());
      }
      return x;
   }

   Expr rel() throws IOException {
      Expr x = expr();
      switch( look.tag ) {
      case '<': case Tag.LE: case Tag.GE: case '>':
         Token tok = look;  move();  return new Rel(tok, x, expr());
      default:
         return x;
      }
   }

   Expr expr() throws IOException {
      Expr x = term();
      while( look.tag == '+' || look.tag == '-' ) {
         Token tok = look;  move();  x = new Arith(tok, x, term());
      }
      return x;
   }

   Expr term() throws IOException {
      Expr x = unary();
      while(look.tag == '*' || look.tag == '/' ) {
         Token tok = look;  move();   x = new Arith(tok, x, unary());
      }
      return x;
   }

   Expr unary() throws IOException {
      if( look.tag == '-' ) {
         move();  return new Unary(Word.minus, unary());
      }
      else if( look.tag == '!' ) {
         Token tok = look;  move();  return new Not(tok, unary());
      }
      else return factor();
   }

   Expr factor() throws IOException {
      Expr x = null;
      switch( look.tag ) {
      case '(':
         move(); x = bool(); match(')');
         return x;
      case Tag.NUM:
         x = new Constant(look, Type.Int);    move(); return x;
      case Tag.REAL:
         x = new Constant(look, Type.Float);  move(); return x;
      case Tag.TRUE:
         x = Constant.True;                   move(); return x;
      case Tag.FALSE:
         x = Constant.False;                  move(); return x;
      default:
         error("syntax error");
         return x;
      case Tag.ID:
         String s = look.toString();
         Id id = top.get(look);
         if( id == null ) error(look.toString() + " undeclared");
         move();
         if( look.tag != '[' ) return id;
         else return offset(id);
      }
   }

   Access offset(Id a) throws IOException {   // I -> [E] | [E] I
      Expr i; Expr w; Expr t1, t2; Expr loc;  // inherit id

      Type type = a.type;
      match('['); i = bool(); match(']');     // first index, I -> [ E ]
      type = ((Array)type).of;
      w = new Constant(type.width);
      t1 = new Arith(new Token('*'), i, w);
      loc = t1;
      while( look.tag == '[' ) {      // multi-dimensional I -> [ E ] I
         match('['); i = bool(); match(']');
         type = ((Array)type).of;
         w = new Constant(type.width);
         t1 = new Arith(new Token('*'), i, w);
         t2 = new Arith(new Token('+'), loc, t1);
         loc = t2;
      }

      return new Access(a, loc, type);
   }

   void emitdata() {
      System.out.println(".data:");
      for (Map.Entry<String, Id> entry : declaredVariables.entrySet()) {
          Id id = entry.getValue();
          String range;
          if (id.range != null) {
              range = id.range.toString();  // e.g., int{0..5}
              System.out.println("  " + id.toString() + " : " + id.type.toString() + range);
          } else {
            System.out.println("  " + id.toString() + " : " + id.type.toString());
          }
      }
  }
}
