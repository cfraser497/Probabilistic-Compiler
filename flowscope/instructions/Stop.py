from .Instruction import Instruction

class Stop(Instruction): # stop
    def __init__(self, labels):
        super().__init__(labels)