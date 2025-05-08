# lexer.py
from tokens import Token, Tag

class Lexer:
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.peek = ' '
        self.words = {
            "iffalse": Token(Tag.IF_FALSE),
            "if": Token(Tag.IF),
            "goto": Token(Tag.GOTO),
            "true": Token(Tag.TRUE),
            "false": Token(Tag.FALSE),
            "flip": Token(Tag.FLIP),
            ".code": Token(Tag.CODE),
            ".data": Token(Tag.DATA),
            "int": Token(Tag.INT),
            "float": Token(Tag.FLOAT),
            "bool": Token(Tag.BOOL),
            "char": Token(Tag.CHAR),
        }

    def readch(self):
        if self.index >= len(self.text):
            self.peek = None
        else:
            self.peek = self.text[self.index]
            self.index += 1

    def readch_match(self, c):
        self.readch()
        if self.peek == c:
            self.peek = ' '
            return True
        return False

    def skip_whitespace(self):
        while self.peek is not None and self.peek in {' ', '\t', '\n', '\r'}:
            self.readch()

    def scan(self):
        self.skip_whitespace()

        if self.peek is None:
            return Token(Tag.EOF)

        # Handle composite operators
        if self.peek in {'<', '>', '=', '!'}:
            char = self.peek
            if self.readch_match('='):
                tok = Token({'<':'<=', '>':'>=', '=':'==', '!': '!='}.get(char))
                return tok
            tok = Token(char)
            self.peek = ' '
            return tok

        if self.peek == '-' or self.peek.isdigit():
            num_str = ''
            if self.peek == '-':
                num_str += '-'
                self.readch()
                if self.peek is None or not self.peek.isdigit():
                    # standalone minus (e.g., as operator)
                    return Token(Tag.MINUS)

            while self.peek is not None and self.peek.isdigit():
                num_str += self.peek
                self.readch()

            if self.peek != '.':
                return Token(Tag.NUM, int(num_str))

            # We have a float
            num_str += self.peek
            self.readch()
            while self.peek is not None and self.peek.isdigit():
                num_str += self.peek
                self.readch()
            return Token(Tag.REAL, float(num_str))

            
        if self.peek == '.':
            self.readch()
            if self.peek == '.':
                self.readch()
                return Token(Tag.SPREAD)
            else:
                # Possibly start of a keyword ".data" or ".code"
                lexeme = '.'
                while self.peek is not None and self.peek.isalnum():
                    lexeme += self.peek
                    self.readch()

                if lexeme in self.words:
                    return self.words[lexeme]

                return Token(Tag.ID, lexeme)

        # Handle identifiers and labels
        if self.peek.isalpha():
            lexeme = ''
            while self.peek is not None and self.peek.isalnum():
                lexeme += self.peek
                self.readch()

            if lexeme in self.words:
                return self.words[lexeme]

            # Check if this is a label (followed by ':')
            if self.peek == ':':
                self.readch()
                return Token(Tag.LABEL, lexeme)

            return Token(Tag.ID, lexeme)

        

        # Single-character tokens
        tok = None
        if self.peek == '=': tok = Token(Tag.ASSIGN)
        elif self.peek == '+': tok = Token(Tag.PLUS)
        elif self.peek == '-': tok = Token(Tag.MINUS)
        elif self.peek == '*': tok = Token(Tag.MUL)
        elif self.peek == '/': tok = Token(Tag.DIV)
        elif self.peek == '[': tok = Token(Tag.LBRACKET)
        elif self.peek == ']': tok = Token(Tag.RBRACKET)
        elif self.peek == ':': tok = Token(Tag.COLON)
        elif self.peek == '{': tok = Token(Tag.LBRACE)
        elif self.peek == '}': tok = Token(Tag.RBRACE)
        elif self.peek == ',': tok = Token(Tag.COMMA)
        elif self.peek == ':': tok = Token(Tag.COLON)

        self.peek = ' '
        if tok:
            return tok

        raise ValueError(f"Unexpected character: {self.peek}")

    def tokens(self):
        tokens = []
        token = self.scan()
        while token.tag != 'EOF':
            tokens.append(token)
            token = self.scan()

        return tokens