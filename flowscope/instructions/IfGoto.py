from .Instruction import Instruction

class IfGoto(Instruction): # if goto LX
    def __init__(self, labels, expr, target_label):
        super().__init__(labels)
        self.expr = expr
        self.target_label = target_label