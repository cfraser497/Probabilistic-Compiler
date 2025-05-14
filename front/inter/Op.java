// package inter;
// import lexer.*; import symbols.*;

// public class Op extends Expr {

//    public Op(Token tok, Type p, Expr x1, Expr x2)  { super(tok, p, x1, x2); }

//    public Expr reduce() {
//       Expr x = gen();
//       // System.out.println("TEST:\n" + x.toString());
//       Temp t = new Temp(type);
//       emit( t.toString() + " = " + x.toString() );
//       // emit(x.toString());
//       // System.out.println(t.toString());
//       return t;
//    }
// }
