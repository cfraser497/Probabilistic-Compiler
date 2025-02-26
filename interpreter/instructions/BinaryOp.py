from .Instruction import Instruction

class BinaryOp(Instruction): # target = arg1 op arg2
    def __init__(self, labels, target, op, arg1, arg2):
        super().__init__(labels)
        self.target = target
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2