from .Instruction import Instruction

class ArrayRead(Instruction):  # x = y[z]
    def __init__(self, labels, target, array_name, index):
        super().__init__(labels)
        self.target = target
        self.array_name = array_name
        self.index = index