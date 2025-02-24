# parser.py
from tokens.tokens import Tag
from instructions import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.lookahead = self.lexer.scan()

    def match(self, tag):
        if self.lookahead.tag == tag:
            self.lookahead = self.lexer.scan()
        else:
            raise SyntaxError(f"Expected {tag}, found {self.lookahead.tag}")

    def parse(self):
        instructions = []
        labels = []

        while True:
            # collect all labels for this line, if any
            while self.lookahead.tag == Tag.LABEL:
                labels.append(self.lookahead.value)
                self.match(Tag.LABEL)

            if self.lookahead.tag == Tag.EOF:
                instructions.append(Empty(labels))
                return instructions

            instruction = self.parse_instruction(labels)
            instructions.append(instruction)
            labels = []

    def parse_instruction(self, labels):
        if self.lookahead.tag == Tag.ID:
            return self.parse_id_starting_instruction(labels)
        elif self.lookahead.tag == Tag.IF_FALSE:
            return self.parse_if_false(labels)
        elif self.lookahead.tag == Tag.GOTO:
            return self.parse_goto(labels)
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
            raise SyntaxError(f"Unexpected token after ID: {self.lookahead.tag}")

    def parse_assign(self, labels, target):
        self.match(Tag.ASSIGN)

        if self.lookahead.tag == Tag.ID:
            source = self.lookahead.value
            self.match(Tag.ID)

            if self.lookahead.tag in (Tag.PLUS, Tag.MINUS, Tag.MUL, Tag.DIV, Tag.LT, Tag.GT, Tag.EQ, Tag.LE, Tag.GE):
                return self.parse_binary_op(labels, target, source)

            elif self.lookahead.tag == Tag.LBRACKET:
                return self.parse_array_read(labels, target, source)

            else:
                return Assign(labels, target, source)

        elif self.lookahead.tag == Tag.NUM:
            source = self.lookahead.value
            self.match(Tag.NUM)
            return Assign(labels, target, source)
        else:
            raise SyntaxError(f"Invalid assignment target: {self.lookahead.tag}")

    def parse_binary_op(self, labels, target, arg1):
        op = self.lookahead.tag
        self.match(op)

        arg2 = self.lookahead.value
        if self.lookahead.tag == Tag.ID:
            self.match(Tag.ID)
        elif self.lookahead.tag == Tag.NUM:
            self.match(Tag.NUM)
        else:
            raise SyntaxError(f"Invalid operand in binary operation: {self.lookahead.tag}")

        return BinaryOp(labels, target, op, arg1, arg2)

    def parse_arr_assign(self, labels, array_name):
        self.match(Tag.LBRACKET)
        index = self.lookahead.value
        if self.lookahead.tag in (Tag.ID, Tag.NUM):
            self.match(self.lookahead.tag)
        else:
            raise SyntaxError("Expected ID or NUM as index")
        self.match(Tag.RBRACKET)

        self.match(Tag.ASSIGN)

        value = self.lookahead.value
        if self.lookahead.tag in (Tag.ID, Tag.NUM):
            self.match(self.lookahead.tag)
        else:
            raise SyntaxError("Expected ID or NUM as value")

        return ArrayAssign(labels, array_name, index, value)

    def parse_array_read(self, labels, target, array_name):
        self.match(Tag.LBRACKET)
        index = self.lookahead.value
        if self.lookahead.tag in (Tag.ID, Tag.NUM):
            self.match(self.lookahead.tag)
        else:
            raise SyntaxError("Expected ID or NUM as array index")
        self.match(Tag.RBRACKET)

        return ArrayRead(labels, target, array_name, index)

    def parse_if_false(self, labels):
        self.match(Tag.IF_FALSE)

        left = self.lookahead.value
        self.match(self.lookahead.tag)

        op = self.lookahead.tag
        if op in (Tag.LT, Tag.GT, Tag.EQ, Tag.LE, Tag.GE):
            self.match(op)
        else:
            raise SyntaxError("Invalid conditional operator in ifFalse")

        right = self.lookahead.value
        self.match(self.lookahead.tag)

        self.match(Tag.GOTO)

        target_label = self.lookahead.value
        self.match(Tag.ID)

        return IfFalseGoto(labels, left, op, right, target_label)

    def parse_if_true(self, labels):
        self.match(Tag.IF_TRUE)

        left = self.lookahead.value
        self.match(self.lookahead.tag)

        op = self.lookahead.tag
        if op in (Tag.LT, Tag.GT, Tag.EQ, Tag.LE, Tag.GE):
            self.match(op)
        else:
            raise SyntaxError("Invalid conditional operator in ifTrue")

        right = self.lookahead.value
        self.match(self.lookahead.tag)

        self.match(Tag.GOTO)

        target_label = self.lookahead.value
        self.match(Tag.ID)

        return IfTrueGoto(labels, left, op, right, target_label)


    def parse_goto(self, labels):
        self.match(Tag.GOTO)
        target_label = self.lookahead.value
        self.match(Tag.ID)
        return Goto(labels, target_label)
