from .Instruction import Instruction

class Goto(Instruction): # goto LX
    def __init__(self, labels, target_label):
        super().__init__(labels)
        self.target_label = target_label