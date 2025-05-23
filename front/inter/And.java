package inter;
import lexer.*;

public class And extends Logical {

   public And(Token tok, Expr x1, Expr x2) { super(tok, x1, x2); }

   public void jumping(int t, int f) {
      int label = f != 0 ? f : newlabel();
      left.jumping(0, label);
      right.jumping(t,f);
      if( f == 0 ) emitlabel(label);
   }
}
