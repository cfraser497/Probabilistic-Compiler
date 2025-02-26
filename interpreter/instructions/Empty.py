from .Instruction import Instruction

class Empty(Instruction): # labels: 
    def __init__(self, labels):
        super().__init__(labels)