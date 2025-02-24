from .Instruction import Instruction

class ArrayAssign(Instruction):  # x[y] = z
    def __init__(self, labels, array_name, index, value):
        super().__init__(labels)
        self.array_name = array_name
        self.index = index
        self.value = value