from .Instruction import Instruction

class IfGoto(Instruction): # if goto LX
    def __init__(self, labels, condition_left, condition_op, condition_right, target_label):
        super().__init__(labels)
        self.left = condition_left
        self.op = condition_op
        self.right = condition_right
        self.target_label = target_label