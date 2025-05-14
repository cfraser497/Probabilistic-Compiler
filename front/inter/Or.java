package inter;
import lexer.*;

public class Or extends Logical {

   public Or(Token tok, Expr x1, Expr x2) { super(tok, x1, x2); }

   public void jumping(int t, int f) {
      int label = t != 0 ? t : newlabel();
      left.jumping(label, 0);
      right.jumping(t,f);
      if( t == 0 ) emitlabel(label);
   }
}
