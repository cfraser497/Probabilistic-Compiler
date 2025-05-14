package inter;
import lexer.*; import symbols.*;

public class Unary extends Expr {

   public Unary(Token tok, Expr x) {    // handles minus, for ! see Not
      super(tok, null, x, null);
      type = Type.max(Type.Int, x.type);
      if (type == null ) error("type error");
   }

   public Expr gen() { return new Unary(op, left.reduce()); }

   public String toString() { return op.toString()+" "+left.toString(); }
}
