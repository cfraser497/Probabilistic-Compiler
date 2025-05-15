package inter;
import lexer.*; import symbols.*;

public class Arith extends Expr {

   public Arith(Token tok, Expr x1, Expr x2)  {
      super(tok, null, x1, x2);
      type = Type.max(x1.type, x2.type);
      if (type == null ) error("type error");
   }

   @Override
   public String toString() {
      int myPrec = getPrecedence(op);

      String leftStr = needsParens(left, myPrec) ? "(" + left + ")" : left.toString();
      String rightStr = needsParens(right, myPrec) ? "(" + right + ")" : right.toString();

      return leftStr + " " + op.toString() + " " + rightStr;
   }

   private boolean needsParens(Expr expr, int parentPrec) {
      if (!(expr instanceof Arith)) return false;
      Token childOp = ((Arith) expr).op;
      return getPrecedence(childOp) < parentPrec;
   }

   private int getPrecedence(Token op) {
      String symbol = op.toString();
      if (symbol.equals("*") || symbol.equals("/")) return 2;
      if (symbol.equals("+") || symbol.equals("-")) return 1;
      return 0;  // for safety, low precedence
   }

}
