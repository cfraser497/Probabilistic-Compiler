package inter;
import lexer.*; import symbols.*;

public class Rel extends Logical {

   public Rel(Token tok, Expr x1, Expr x2) { super(tok, x1, x2); }

   public Type check(Type p1, Type p2) {
      if ( p1 instanceof Array || p2 instanceof Array ) return null;
      else if( p1 == p2 ) return Type.Bool;
      else return null;
   }

   public void jumping(int t, int f) {
      Expr a = left.reduce();
      Expr b = right.reduce();
      String test = a.toString() + " " + op.toString() + " " + b.toString();
      emitjumps(test, t, f);
   }
}
