# parser.py
from tokens.tokens import Tag
from instructions import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.lookahead = self.lexer.scan()
        self.variables = {}  # name → dict with 'type', 'range', 'values', etc.

    def match(self, tag):
        if self.lookahead.tag == tag:
            self.lookahead = self.lexer.scan()
            # print(self.lookahead.tag)
        else:
            raise SyntaxError(f"Expected {tag}, found {self.lookahead.tag}")

    def parse(self):
        self.match(Tag.DATA)
        self.match(Tag.COLON)
        self.parse_data()

        self.match(Tag.CODE)
        self.match(Tag.COLON)

        instructions = []
        labels = []

        while True:
            while self.lookahead.tag == Tag.LABEL:
                labels.append(self.lookahead.value)
                self.match(Tag.LABEL)

            if self.lookahead.tag == Tag.EOF:
                instructions.append(Empty(labels))
                return instructions, self.variables

            instruction = self.parse_instruction(labels)
            instructions.append(instruction)
            labels = []

    def parse_data(self):
        while self.lookahead.tag == Tag.ID:
            var_info = {
                "dims": [],
                "range": None,
                "type": None
            }

            varname = self.lookahead.value
            self.match(Tag.ID)
            self.match(Tag.COLON)

            while self.lookahead.tag == Tag.LBRACKET:
                self.match(Tag.LBRACKET)
                dim_size = self.lookahead.value
                self.match(Tag.NUM)
                self.match(Tag.RBRACKET)
                var_info["dims"].append(dim_size)


            base_type = self.lookahead.tag
            var_info["type"] = base_type
            self.match(base_type)

            if self.lookahead.tag == Tag.LBRACE:
                self.match(Tag.LBRACE)
                values = []

                if self.lookahead.tag == Tag.NUM:
                    first = self.lookahead.value
                    self.match(Tag.NUM)

                    if self.lookahead.tag == Tag.SPREAD:
                        self.match(Tag.SPREAD)
                        last = self.lookahead.value
                        self.match(Tag.NUM)
                        var_info["range"] = (first, last)
                    else:
                        values.append(first)
                        while self.lookahead.tag == Tag.COMMA:
                            self.match(Tag.COMMA)
                            val = self.lookahead.value
                            self.match(Tag.NUM)
                            values.append(val)
                        var_info["range"] = values

                self.match(Tag.RBRACE)

            self.variables[varname] = var_info

    def parse_instruction(self, labels):
        if self.lookahead.tag == Tag.ID:
            return self.parse_id_starting_instruction(labels)
        elif self.lookahead.tag == Tag.IF or self.lookahead.tag == Tag.IF_FALSE:
            return self.parse_if(labels)
        elif self.lookahead.tag == Tag.GOTO:
            return self.parse_goto(labels)
        elif self.lookahead.tag == Tag.FLIP:
            return self.parse_flip(labels)
        else:
            raise SyntaxError(f"Unexpected token: {self.lookahead.tag}")

    def parse_id_starting_instruction(self, labels):
        target = self.lookahead.value
        self.match(Tag.ID)

        if self.lookahead.tag == Tag.ASSIGN:
            return self.parse_assign(labels, target)
        elif self.lookahead.tag == Tag.LBRACKET:
            return self.parse_arr_assign(labels, target)
        else:
            print(self.lookahead.tag)
            raise SyntaxError(f"Unexpected token after ID: {self.lookahead.tag}")

    def parse_signed_op(self, allow_real=True, allow_bool=True):
        tag, value = self.lookahead.tag, self.lookahead.value
        if allow_bool and tag == Tag.TRUE or tag == Tag.FALSE:
            self.match(tag)
            return tag

        sign = 1
        if self.lookahead.tag == Tag.MINUS:
            self.match(Tag.MINUS)
            sign = -1
        
        if self.lookahead.tag == Tag.NUM:
            value = self.lookahead.value
            self.match(Tag.NUM)
            return sign * value
        
        elif allow_real and self.lookahead.tag == Tag.REAL:
            value = self.lookahead.value
            self.match(Tag.REAL)
            return sign * value

        elif self.lookahead.tag == Tag.ID:
            value = self.lookahead.value
            self.match(Tag.ID)
            if sign == -1:
                return f"-{value}"
            return value
        else:
            raise SyntaxError(f"Unexpected Tag, got {self.lookahead.tag}")



    def parse_assign(self, labels, target):
        self.match(Tag.ASSIGN)

        source = self.parse_signed_op()

        if self.lookahead.tag in (Tag.PLUS, Tag.MINUS, Tag.MUL, Tag.DIV, Tag.LT, Tag.GT, Tag.EQ, Tag.LE, Tag.GE):
            return self.parse_binary_op(labels, target, source)

        elif self.lookahead.tag == Tag.LBRACKET:
            return self.parse_array_read(labels, target, source)

        return Assign(labels, target, source)


    def parse_binary_op(self, labels, target, arg1):
        op = self.lookahead.tag
        self.match(op)

        arg2 = self.parse_signed_op()

        return BinaryOp(labels, target, op, arg1, arg2)

    def parse_arr_assign(self, labels, array_name):
        self.match(Tag.LBRACKET)
        index = self.parse_signed_op(allow_real=False, allow_bool=False)
        self.match(Tag.RBRACKET)

        self.match(Tag.ASSIGN)

        value = self.parse_signed_op()

        return ArrayAssign(labels, array_name, index, value)

    def parse_array_read(self, labels, target, array_name):
        self.match(Tag.LBRACKET)
        index = self.parse_signed_op(allow_bool=False, allow_real=False)
        self.match(Tag.RBRACKET)

        return ArrayRead(labels, target, array_name, index)

    def parse_if(self, labels):
        iftag = self.lookahead.tag
        self.match(iftag)

        left = self.lookahead.value
        self.match(self.lookahead.tag)

        if self.lookahead.tag in (Tag.LT, Tag.GT, Tag.EQ, Tag.LE, Tag.GE, Tag.NEQ):
            op = self.lookahead.tag
            self.match(op)

            right = self.lookahead.value
            self.match(self.lookahead.tag)
        else:
            # Boolean only: e.g. if b goto L2
            op = None
            right = None

        self.match(Tag.GOTO)
        target_label = self.lookahead.value
        self.match(Tag.ID)

        if iftag == Tag.IF:
            return IfGoto(labels, left, op, right, target_label)
        return IfFalseGoto(labels, left, op, right, target_label)

    def parse_goto(self, labels):
        self.match(Tag.GOTO)
        target_label = self.lookahead.value
        self.match(Tag.ID)
        return Goto(labels, target_label)
    
    def parse_flip(self, labels):
        self.match(Tag.FLIP)
        weights = []
        target_labels = []

        while self.lookahead.tag != Tag.LABEL:
            weight = self.lookahead.value
            weights.append(weight)
            self.match(Tag.NUM)

            self.match(Tag.GOTO)
            label = self.lookahead.value
            target_labels.append(label)
            self.match(Tag.ID)

        return Flip(labels, weights, target_labels)
