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
        if isinstance(identifier, int) or isinstance(identifier, float):
            return identifier
        if isinstance(identifier, str) and identifier.isdigit():
            return int(identifier)
        # handle negative values e.g. -x
        if identifier[0] == "-":
            return self.memory.get(identifier[1:])
        if identifier == Tag.TRUE or identifier == Tag.FALSE:
            return identifier
        return self.memory.get(identifier)

    def set_value(self, identifier, value):
        self.memory[identifier] = value
