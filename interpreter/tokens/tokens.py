class Token:
    def __init__(self, tag, value=None):
        self.tag = tag
        self.value = value

    def __repr__(self):
        return f"{self.tag}({self.value})" if self.value is not None else f"{self.tag}"

class Tag:
    NUM = 'NUM'
    REAL = 'REAL'
    ID = 'ID'
    LABEL = 'LABEL'
    ASSIGN = '='
    PLUS = '+'
    MINUS = '-'
    MUL = '*'
    DIV = '/'
    LT = '<'
    GT = '>'
    EQ = '=='
    LE = '<='
    GE = '>='
    NEQ = '!='
    LBRACKET = '['
    RBRACKET = ']'
    IF = 'if'
    IF_FALSE = 'ifFalse'
    GOTO = 'goto'
    COLON = ':'
    EOF = 'EOF'
    TRUE = 'true'
    FALSE = 'false'
