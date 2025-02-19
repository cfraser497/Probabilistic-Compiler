package inter;

public class Branch extends Node{
    
    int prob; Stmt stmt; int label;

    public Branch(int prob, Stmt stmt) {
        this.prob = prob; this.stmt = stmt;
    }

    public void gen(int f, boolean isFinal) {
        emitlabel(label);
        stmt.gen(label, f);
        if (!isFinal) emit("goto L" + f);
    }

    public int getProb() {
        return prob;
    }

    public void setLabel(int label) {
        this.label = label;
    }
}
