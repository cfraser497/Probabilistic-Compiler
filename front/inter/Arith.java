package inter;
import lexer.*; import symbols.*;

public class Arith extends Expr {

   public Arith(Token tok, Expr x1, Expr x2)  {
      super(tok, null, x1, x2);
      type = Type.max(x1.type, x2.type);
      if (type == null ) error("type error");
   }

   public String toString() {
      return left.toString()+" "+op.toString()+" "+right.toString();
   }
}
