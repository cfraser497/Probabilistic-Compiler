# interpreter.py
from instructions import *

def execute(env):
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
                '==': lambda a, b: int(a == b)
            }
            result = ops[instr.op](env.get_value(instr.arg1), env.get_value(instr.arg2))
            env.set_value(instr.target, result)

        elif isinstance(instr, IfFalseGoto):
            condition = {
                '<': lambda a, b: a < b, '>': lambda a, b: a > b,
                '<=': lambda a, b: a <= b, '>=': lambda a, b: a >= b,
                '==': lambda a, b: a == b
            }[instr.condition_op](env.get_value(instr.condition_left), env.get_value(instr.condition_right))

            if not condition:
                print(env.labels)
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

        env.pc += 1
