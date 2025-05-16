# parser.py
from tokens import Tag
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

        while self.lookahead.tag != Tag.EOF:

            while self.lookahead.tag == Tag.LABEL:
                labels.append(self.lookahead.value)
                self.match(Tag.LABEL)

            instruction = self.parse_instruction(labels)
            instructions.append(instruction)
            labels = []

        instructions.append(Empty(labels))
        return instructions, self.variables
    

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
        elif self.lookahead.tag == Tag.STOP:
            return self.parse_stop(labels)
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

    def parse_assign(self, labels, target):
        self.match(Tag.ASSIGN)
        expr = self.parse_expr()
        return Assign(labels, target, expr)
    
    def parse_expr(self):
        return self.parse_or()
    
    def parse_or(self):
        expr = self.parse_and()
        while self.lookahead.tag == Tag.OR:
            op = self.lookahead.tag
            self.match(op)
            right = self.parse_and()
            expr = ('binop', op, expr, right)
        return expr

    def parse_and(self):
        expr = self.parse_rel()
        while self.lookahead.tag == Tag.AND:
            op = self.lookahead.tag
            self.match(op)
            right = self.parse_rel()
            expr = ('binop', op, expr, right)
        return expr
    
    def parse_rel(self):
        expr = self.parse_arith_expr()
        while self.lookahead.tag in (Tag.LT, Tag.LE, Tag.GT, Tag.GE, Tag.EQ, Tag.NEQ):
            op = self.lookahead.tag
            self.match(op)
            right = self.parse_arith_expr()
            expr = ('binop', op, expr, right)
        return expr

    def parse_arith_expr(self):
        expr = self.parse_term()
        while self.lookahead.tag in (Tag.PLUS, Tag.MINUS):
            op = self.lookahead.tag
            self.match(op)
            right = self.parse_term()
            expr = ('binop', op, expr, right)
        return expr

    def parse_term(self):
        expr = self.parse_unary()
        while self.lookahead.tag in (Tag.MUL, Tag.DIV):
            op = self.lookahead.tag
            self.match(op)
            right = self.parse_unary()
            expr = ('binop', op, expr, right)
        return expr

    def parse_unary(self):
        if self.lookahead.tag == Tag.MINUS:
            self.match(Tag.MINUS)
            expr = self.parse_unary()
            return ('neg', expr)
        elif self.lookahead.tag == Tag.NOT:
            self.match(Tag.NOT)
            expr = self.parse_unary()
            return ('not', expr)
        return self.parse_factor()


    def parse_factor(self):
        if self.lookahead.tag == Tag.LPAREN:
            self.match(Tag.LPAREN)
            expr = self.parse_expr()
            self.match(Tag.RPAREN)
            return expr
        elif self.lookahead.tag == Tag.NUM:
            value = self.lookahead.value
            self.match(Tag.NUM)
            return ('num', value)
        elif self.lookahead.tag == Tag.REAL:
            value = self.lookahead.value
            self.match(Tag.REAL)
            return ('real', value)
        elif self.lookahead.tag == Tag.TRUE:
            self.match(Tag.TRUE)
            return ('bool', True)
        elif self.lookahead.tag == Tag.FALSE:
            self.match(Tag.FALSE)
            return ('bool', False)
        elif self.lookahead.tag == Tag.ID:
            name = self.lookahead.value
            self.match(Tag.ID)
            if self.lookahead.tag == Tag.LBRACKET:
                self.match(Tag.LBRACKET)
                index_expr = self.parse_expr()
                self.match(Tag.RBRACKET)
                return ('array', name, index_expr)
            return ('var', name)
        else:
            raise SyntaxError(f"Unexpected token in expression: {self.lookahead.tag}")



    def parse_arr_assign(self, labels, array_name):
        self.match(Tag.LBRACKET)
        index_expr = self.parse_expr()
        self.match(Tag.RBRACKET)
        self.match(Tag.ASSIGN)
        value_expr = self.parse_expr()
        return ArrayAssign(labels, array_name, index_expr, value_expr)


    def parse_array_read(self, labels, target, array_name):
        self.match(Tag.LBRACKET)
        index_expr = self.parse_expr()
        self.match(Tag.RBRACKET)
        return ArrayRead(labels, target, array_name, index_expr)

    def parse_if(self, labels):
        iftag = self.lookahead.tag
        self.match(iftag)

        # Parse full expression instead of just identifier
        condition_expr = self.parse_expr()

        self.match(Tag.GOTO)
        target_label = self.lookahead.value
        self.match(Tag.ID)

        if iftag == Tag.IF:
            return IfGoto(labels, condition_expr, target_label)
        return IfFalseGoto(labels, condition_expr, target_label)


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


    def parse_stop(self, labels):
        self.match(Tag.STOP)
        return Stop(labels)