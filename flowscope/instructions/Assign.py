from .Instruction import Instruction

class Assign(Instruction): # target = source
    def __init__(self, labels, target, source):
        super().__init__(labels)
        self.target = target
        self.source = source
