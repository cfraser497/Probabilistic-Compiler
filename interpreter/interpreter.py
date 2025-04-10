# interpreter.py
from instructions import *
from tokens.tokens import Tag
import random

def execute(env, seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Interperate Program!
    while env.pc < len(env.instructions):
        instr = env.instructions[env.pc]

        if isinstance(instr, Assign):
            env.set_value(instr.target, env.get_value(instr.source))

        elif isinstance(instr, BinaryOp):
            ops = {
                '+': lambda a, b: a + b, '-': lambda a, b: a - b,
                '*': lambda a, b: a * b, '/': lambda a, b: a // b,
                '<': lambda a, b: int(a < b), '>': lambda a, b: int(a > b),
                '<=': lambda a, b: int(a <= b), '>=': lambda a, b: int(a >= b),
                '==': lambda a, b: int(a == b), '!=': lambda a, b: int(a != b)
            }
            # print(f"ARG1: {env.get_value(instr.arg1)}")
            # print(f"ARG2: {env.get_value(instr.arg2)}")
            result = ops[instr.op](env.get_value(instr.arg1), env.get_value(instr.arg2))
            env.set_value(instr.target, result)

        elif isinstance(instr, IfGoto):
            if evaluate_condition(instr, env):
                env.pc = env.labels[instr.target_label]
                continue

        elif isinstance(instr, IfFalseGoto):
            if not evaluate_condition(instr, env):
                env.pc = env.labels[instr.target_label]
                continue

        elif isinstance(instr, Goto):
            env.pc = env.labels[instr.target_label]
            continue

        elif isinstance(instr, ArrayAssign):
            idx = env.get_value(instr.index)
            val = env.get_value(instr.value)
            env.arrays.setdefault(instr.array_name, {})[idx] = val

        elif isinstance(instr, ArrayRead):
            idx = env.get_value(instr.index)
            val = env.arrays.get(instr.array_name, {}).get(idx, 0)
            env.set_value(instr.target, val)

        elif isinstance(instr, Flip):
            target_label = random.choices(instr.target_labels, weights=instr.weights, k=1)[0]
            env.pc = env.labels[target_label]
            continue

        elif isinstance(instr, Empty):
            pass

        else:
            raise SyntaxError("Unknown Instruction: " + instr.__class__.__name__)

        env.pc += 1

        # print(f"{env.pc}: {env.memory}")


def evaluate_condition(instr, env):
    if instr.op is None:
        # Boolean-only conditional: use left as boolean value
        return True if env.get_value(instr.left) == Tag.TRUE else False
    else:
        a = env.get_value(instr.left)
        b = env.get_value(instr.right)

        op_func = {
            '<': lambda x, y: x < y,
            '>': lambda x, y: x > y,
            '<=': lambda x, y: x <= y,
            '>=': lambda x, y: x >= y,
            '==': lambda x, y: x == y,
            '!=': lambda x, y: x != y
        }[instr.op]
        return op_func(a, b)