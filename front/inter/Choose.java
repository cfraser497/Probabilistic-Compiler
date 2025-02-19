package inter;

import inter.*;
import java.util.List;

public class Choose extends Stmt {
    List<Branch> branches;
    int totalWeight;

    public Choose(List<Branch> branches, int totalWeight) {
        this.branches = branches;
        this.totalWeight = totalWeight;
    }

    @Override
    public void gen(int b, int a) {
        int totalBranches = branches.size();
        
        if (totalBranches == 0) return;

        // reserve all branch labels as we create our flip instruction
        StringBuilder flipInstruction = new StringBuilder("flip ");
        for (int i = 0; i < branches.size(); i++) {
            Branch branch = branches.get(i);

            int label = newlabel();
            branch.setLabel(label);
            flipInstruction.append(branch.getProb() + "/" + totalWeight + " goto L" + label);
            if (i != branches.size() - 1) {
                flipInstruction.append(" ");
            }
        }

        emit(flipInstruction.toString());
        boolean isFinal = false;

        for (int i = 0; i < branches.size(); i++) {
            if (i == branches.size() - 1) isFinal = true;
            
            Branch branch = branches.get(i);
            branch.gen(a, isFinal);
        }
    }
}
