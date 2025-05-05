from .Instruction import Instruction

class Flip(Instruction): # flip num goto L1 2 num goto L2
    def __init__(self, labels, weights, target_labels):
        super().__init__(labels)
        self.weights = weights
        self.target_labels = target_labels