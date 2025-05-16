from instructions import *
from tokens import Tag
import random

class Executor:
    def __init__(self, env, seed=None):
        self.env = env
        if seed is not None:
            random.seed(seed)

    def run(self):
        while self.env.pc < len(self.env.instructions):
            instr = self.env.instructions[self.env.pc]

            if isinstance(instr, Assign):
                value = instr.source.eval(self.env)
                self.validate(instr.target, value)
                self.env.set_value(instr.target, value)

            elif isinstance(instr, ArrayAssign):
                index = instr.index.eval(self.env)
                value = instr.value.eval(self.env)
                self.validate(instr.array_name, value)
                if index < 0:
                    raise RuntimeError(f"Invalid array index: {index}")
                self.env.arrays.setdefault(instr.array_name, {})[index] = value

            elif isinstance(instr, ArrayRead):
                index = instr.index.eval(self.env)
                value = self.env.arrays.get(instr.array_name, {}).get(index, 0)
                self.validate(instr.target, value)
                self.env.set_value(instr.target, value)

            elif isinstance(instr, IfGoto):
                if instr.expr.eval(self.env) == Tag.TRUE:
                    self.env.pc = self.env.labels[instr.target_label]
                    continue

            elif isinstance(instr, IfFalseGoto):
                if instr.expr.eval(self.env) != Tag.TRUE:
                    self.env.pc = self.env.labels[instr.target_label]
                    continue

            elif isinstance(instr, IfGoto):
                if self.evaluate_condition(instr):
                    self.env.pc = self.env.labels[instr.target_label]
                    continue

            elif isinstance(instr, IfFalseGoto):
                if not self.evaluate_condition(instr):
                    self.env.pc = self.env.labels[instr.target_label]
                    continue

            elif isinstance(instr, Goto):
                self.env.pc = self.env.labels[instr.target_label]
                continue

            elif isinstance(instr, Flip):
                chosen = random.choices(instr.target_labels, weights=instr.weights, k=1)[0]
                self.env.pc = self.env.labels[chosen]
                continue

            elif isinstance(instr, Stop):
                self.env.pc = len(self.env.instructions)

            elif isinstance(instr, Empty):
                pass

            else:
                raise RuntimeError(f"Unknown instruction type: {instr}")

            self.env.pc += 1

    def validate(self, name, value):
        if name not in self.env.variables:
            return  # unknown variable, ignore for now

        meta = self.env.variables[name]
        expected_type = meta["type"]
        allowed_range = meta.get("range")

        # Type enforcement
        if expected_type == Tag.INT and not isinstance(value, int):
            raise RuntimeError(f"Type error: {name} expects int, got {value}")
        elif expected_type == Tag.FLOAT and not isinstance(value, float):
            raise RuntimeError(f"Type error: {name} expects float, got {value}")
        elif expected_type == Tag.BOOL and value not in (Tag.TRUE, Tag.FALSE):
            raise RuntimeError(f"Type error: {name} expects bool, got {value}")

        # Range enforcement
        if allowed_range is not None:
            if isinstance(allowed_range, tuple):
                if not (allowed_range[0] <= value <= allowed_range[1]):
                    raise RuntimeError(f"Range error: {name} value {value} not in {allowed_range}")
            elif isinstance(allowed_range, list):
                if value not in allowed_range:
                    raise RuntimeError(f"Value error: {name} value {value} not in {allowed_range}")

    def evaluate_condition(self, instr):
        if instr.op is None:
            return self.env.get_value(instr.left) == Tag.TRUE
        a = self.env.get_value(instr.left)
        b = self.env.get_value(instr.right)
        return {
            '<': lambda x, y: x < y,
            '>': lambda x, y: x > y,
            '<=': lambda x, y: x <= y,
            '>=': lambda x, y: x >= y,
            '==': lambda x, y: x == y,
            '!=': lambda x, y: x != y
        }[instr.op](a, b)
