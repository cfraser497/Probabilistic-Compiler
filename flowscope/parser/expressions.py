from tokens import Tag 

class Expr:
    def eval(self, _): raise NotImplementedError
    def __repr__(self): return self.__str__()

class Number(Expr):
    def __init__(self, value): self.value = value
    def __str__(self): return str(self.value)
    def eval(self, _): return self.value

class Real(Expr):
    def __init__(self, value): self.value = value
    def __str__(self): return str(self.value)
    def eval(self, _): return self.value

class Boolean(Expr):
    def __init__(self, value): self.value = value
    def __str__(self): return "true" if self.value else "false"
    def eval(self, _): return Tag.TRUE if self.value else Tag.FALSE

class Variable(Expr):
    def __init__(self, name): self.name = name
    def __str__(self): return self.name
    def eval(self, env): return env.get_value(self.name)

class ArrayAccess(Expr):
    def __init__(self, array_name, index): self.array_name = array_name; self.index = index
    def __str__(self): return f"{self.array_name}[{self.index}]"
    def eval(self, env): return env.arrays.get(self.array_name, {}).get(self.index.eval(env), 0)

class UnaryOp(Expr):
    def __init__(self, op, expr): self.op = op; self.expr = expr
    def __str__(self): return f"({self.op} {self.expr})"
    def eval(self, env):
        v = self.expr.eval(env)
        if self.op == Tag.MINUS: return -v
        if self.op == Tag.NOT: return Tag.FALSE if v == Tag.TRUE else Tag.TRUE
        raise RuntimeError(f"Unsupported unary op: {self.op}")

class BinaryOp(Expr):
    def __init__(self, op, left, right): self.op = op; self.left = left; self.right = right
    def __str__(self): return f"({self.left} {self.op} {self.right})"
    def eval(self, env):
        l = self.left.eval(env)
        r = self.right.eval(env)
        # as per your eval_binary logic
        return self._eval_binary(self.op, l, r)

    def _eval_binary(self, op, a, b):
        ops = {
            Tag.PLUS: lambda x, y: x + y,
            Tag.MINUS: lambda x, y: x - y,
            Tag.MUL: lambda x, y: x * y,
            Tag.DIV: lambda x, y: x // y,
            Tag.LT: lambda x, y: Tag.TRUE if x < y else Tag.FALSE,
            Tag.GT: lambda x, y: Tag.TRUE if x > y else Tag.FALSE,
            Tag.LE: lambda x, y: Tag.TRUE if x <= y else Tag.FALSE,
            Tag.GE: lambda x, y: Tag.TRUE if x >= y else Tag.FALSE,
            Tag.EQ: lambda x, y: Tag.TRUE if x == y else Tag.FALSE,
            Tag.NEQ: lambda x, y: Tag.TRUE if x != y else Tag.FALSE,
            Tag.OR: lambda x, y: Tag.TRUE if x == Tag.TRUE or y == Tag.TRUE else Tag.FALSE,
            Tag.AND: lambda x, y: Tag.TRUE if x == Tag.TRUE and y == Tag.TRUE else Tag.FALSE,
        }

        if op not in ops:
            raise RuntimeError(f"Unsupported binary operator: {op}")
        return ops[op](a, b)
