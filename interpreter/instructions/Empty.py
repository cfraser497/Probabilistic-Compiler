from .Instruction import Instruction

class Empty(Instruction):
    def __init__(self, labels):
        super().__init__(labels)