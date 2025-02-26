from .Instruction import Instruction

class IfFalseGoto(Instruction): # iffalse goto LX
    def __init__(self, labels, condition_left, condition_op, condition_right, target_label):
        super().__init__(labels)
        self.condition_left = condition_left
        self.condition_op = condition_op
        self.condition_right = condition_right
        self.target_label = target_label