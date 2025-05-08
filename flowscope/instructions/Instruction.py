class Instruction:
    def __init__(self, labels):
        self.labels = labels

    def __str__(self):
        return f"{self.__class__.__name__} {vars(self)}"

