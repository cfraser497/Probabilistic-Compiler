package inter;
import lexer.*;

public class Not extends Logical {

   public Not(Token tok, Expr x2) { super(tok, x2, x2); }

   public void jumping(int t, int f) { right.jumping(f, t); }

   public String toString() { return op.toString()+" "+right.toString(); }
}
