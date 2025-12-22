from tokens import Token, TokenType

STR_NEW_LINE = '\n'
STR_EOF = '\0'
STR_LPAREN = '('
STR_RPAREN = ')'
STR_LBRACE = '{'
STR_RBRACE = '}'
STR_COLON = ':'
STR_COMMA = ','
STR_ARROW = '>'  # '->'
STR_PLUS = '+'
STR_MINUS = '-'
STR_ASSIGN = '='

class Lexer:
    def __init__(self, source_code: str):
        self.source = source_code
        self.source_length = len(source_code)
        self.tokens = []
        self.cursor = 0
        self.line = 1
        self.col = 1

    def is_at_end(self) -> bool:
        return self.cursor >= self.source_length

    def advance(self) -> str:
        current_character = self.source[self.cursor]
        self.cursor += 1

        if current_character == STR_NEW_LINE:
            self.line += 1
            self.col = 1
        else:
            self.col += 1

        return current_character

    def peek(self) -> str:
        if self.is_at_end():
            return STR_EOF
        return self.source[self.cursor]

    def peek_next(self) -> str:
        if self.cursor + 1 >= self.source_length:
            return STR_EOF
        return self.source[self.cursor + 1]

    def skip_whitespace(self):
        while self.peek().isspace():
            self.advance()

    def scan_identifier(self, first_char):
        value = first_char
        while self.peek().isalnum() or self.peek() == '_':
            value += self.advance()
        return value

    def scan_number(self, first_char):
        value = first_char
        while self.peek().isdigit():
            value += self.advance()
        return value

    def add_token(self, token_type, token_value, line, column):
        self.tokens.append(
            Token(
                token_type,
                token_value,
                line,
                column
            )
        )

    @property
    def tokenize(self) -> list[Token]:
        while not self.is_at_end():
            if self.peek().isspace():
                self.skip_whitespace()
                if self.is_at_end():
                    break

            current_line = self.line
            current_col = self.col
            character = self.advance()

            if character.isdigit():
                val = self.scan_number(character)
                self.add_token(TokenType.NUMBER, val, current_line, current_col)

            # keywords and identifiers
            elif character.isalpha() or character == '_':
                val = self.scan_identifier(character)
                # Keywords
                if val == "fn":
                    self.add_token(TokenType.FN, val, current_line, current_col)
                elif val == "return":
                    self.add_token(TokenType.RETURN, val, current_line, current_col)
                elif val == "let":
                    self.add_token(TokenType.LET, val, current_line, current_col)
                elif val == "const":
                    self.add_token(TokenType.CONST, val, current_line, current_col)
                else:
                    self.add_token(TokenType.IDENTIFIER, val, current_line, current_col)

            # Symbols
            elif character == STR_LPAREN:
                self.add_token(TokenType.LPAREN, character, current_line, current_col)
            elif character == STR_RPAREN:
                self.add_token(TokenType.RPAREN, character, current_line, current_col)
            elif character == STR_LBRACE:
                self.add_token(TokenType.LBRACE, character, current_line, current_col)
            elif character == STR_RBRACE:
                self.add_token(TokenType.RBRACE, character, current_line, current_col)
            elif character == STR_COLON:
                self.add_token(TokenType.COLON, character, current_line, current_col)
            elif character == STR_ASSIGN:
                self.add_token(TokenType.ASSIGN, character, current_line, current_col)
            elif character == STR_COMMA:
                self.add_token(TokenType.COMMA, character, current_line, current_col)
            elif character == STR_PLUS:
                self.add_token(TokenType.PLUS, character, current_line, current_col)
            elif character == STR_MINUS:
                # Verifica se é uma seta '->'
                if self.peek() == STR_ARROW:
                    self.advance()  # Consome o '>'
                    self.add_token(TokenType.ARROW, "->", current_line, current_col)
                else:
                    self.add_token(TokenType.MINUS, character, current_line, current_col)

        self.add_token(TokenType.EOF, STR_EOF, self.line, self.col)
        return self.tokens