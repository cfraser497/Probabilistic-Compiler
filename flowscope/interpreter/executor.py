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
                val = self.env.get_value(instr.source)
                self.validate(instr.target, val)
                self.env.set_value(instr.target, val)

            elif isinstance(instr, BinaryOp):
                result = self.eval_binary(instr.op, self.env.get_value(instr.arg1), self.env.get_value(instr.arg2))
                self.validate(instr.target, result)
                self.env.set_value(instr.target, result)

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

            elif isinstance(instr, ArrayAssign):
                idx = self.env.get_value(instr.index)
                val = self.env.get_value(instr.value)
                self.validate(instr.array_name, val)
                if idx < 0:
                    raise RuntimeError(f"Invalid array index: {idx}")
                self.env.arrays.setdefault(instr.array_name, {})[idx] = val

            elif isinstance(instr, ArrayRead):
                idx = self.env.get_value(instr.index)
                val = self.env.arrays.get(instr.array_name, {}).get(idx, 0)
                self.validate(instr.target, val)
                self.env.set_value(instr.target, val)

            elif isinstance(instr, Flip):
                target_label = random.choices(instr.target_labels, weights=instr.weights, k=1)[0]
                self.env.pc = self.env.labels[target_label]
                continue

            elif isinstance(instr, Empty):
                pass

            elif isinstance(instr, Stop):
                # set the program counter out of range, terminating execution
                self.env.pc = len(self.env.instructions)

            else:
                raise SyntaxError("Unknown Instruction: " + instr.__class__.__name__)

            self.env.pc += 1

    def validate(self, name, value):
        if name not in self.env.variables:
            return  # unknown variable

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

    def eval_binary(self, op, a, b):
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x // y,
            '<': lambda x, y: int(x < y),
            '>': lambda x, y: int(x > y),
            '<=': lambda x, y: int(x <= y),
            '>=': lambda x, y: int(x >= y),
            '==': lambda x, y: int(x == y),
            '!=': lambda x, y: int(x != y)
        }
        return ops[op](a, b)

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
