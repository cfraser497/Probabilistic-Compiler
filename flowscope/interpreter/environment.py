from tokens import Tag

class Environment:
    def __init__(self, instructions, variables):
        self.memory = {}
        self.arrays = {}
        self.variables = variables
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
        if isinstance(identifier, (int, float)):
            return identifier
        if isinstance(identifier, str):
            if identifier == Tag.TRUE or identifier == Tag.FALSE:
                return identifier
            if identifier.isdigit() or (identifier[0] == '-' and identifier[1:].isdigit()):
                return int(identifier)
            if identifier.startswith('-') and identifier[1:] in self.memory:
                return -self.memory.get(identifier[1:], 0)
            return self.memory.get(identifier, 0)
        return identifier


    def set_value(self, identifier, value):
        self.memory[identifier] = value
