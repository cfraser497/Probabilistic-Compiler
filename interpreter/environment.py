class Environment:
    def __init__(self, instructions):
        self.memory = {}
        self.arrays = {}
        self.labels = self.map_labels(instructions)
        self.instructions = instructions
        self.pc = 0

    def map_labels(self, instructions):
        labels = {}
        for idx, instr in enumerate(instructions):
            for label in instr.labels:
                labels[label] = idx
        return labels

    def get_value(self, identifier):
        if isinstance(identifier, int):
            return identifier
        if isinstance(identifier, str) and identifier.isdigit():
            return int(identifier)
        return self.memory.get(identifier, 0)

    def set_value(self, identifier, value):
        self.memory[identifier] = value
