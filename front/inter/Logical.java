package inter;
import lexer.*; import symbols.*;

public class Logical extends Expr {

   Logical(Token tok, Expr x1, Expr x2) {
      super(tok, null, x1, x2);                      // null type to start
      type = check(x1.type, x2.type);
      if (type == null ) error("type error");
   }

   public Type check(Type p1, Type p2) {
      if ( p1 == Type.Bool && p2 == Type.Bool ) return Type.Bool;
      else return null;
   }
}
