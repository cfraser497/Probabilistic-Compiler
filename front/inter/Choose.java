package inter;

public class Choose extends Stmt {
    Brnchs branches;

    public Choose(Brnchs bs) {
       branches = bs;
    }
 
    public void gen(int b, int a) {
    //    int label = newlabel(); // label for the code for stmt
    //    expr.jumping(0, a);     // fall through on true, goto a on false
    //    emitlabel(label); stmt.gen(label, a);
    }
}
