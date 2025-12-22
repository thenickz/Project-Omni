from tokens import Token, TokenType
from dataclasses import dataclass


class Node:
    pass


class Expr(Node):
    """Expression Node like 1+1"""
    pass


class Stmt(Node):
    """Statement Node like if, return"""
    pass


@dataclass
class TypeNode(Node):
    name: str


@dataclass
class VarDeclaration(Stmt):
    name: str
    var_type: TypeNode
    value: Expr

@dataclass
class BinaryExpr(Expr):
    left: Expr
    operator: str
    right: Expr
@dataclass
class Identifier(Expr):
    name:str

@dataclass
class IntLiteral(Expr):
    value: int


@dataclass
class FunctionDeclaration:
    pass


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.cursor = 0

    def is_at_end(self):
        return self.peek().type == TokenType.EOF

    def advance(self) -> Token | None:
        if not self.is_at_end():
            self.cursor += 1
        return self.tokens[self.cursor - 1]

    def peek(self) -> Token:
        return self.tokens[self.cursor]

    def consume(self, expected_type: TokenType|None, message: str = "Not implemented yet" ) -> Token:
        t = self.peek()
        if t.type == expected_type:
            return self.advance()

        error_mensade = f"""|               Parser Error has occurred.             |
        |------------------------------------------------------|
        |- [Syntax Error] Line: {t.line}, Column: {t.column}:" |
        |- Found: {t.type.name} ('{t.value}').                 |
        |- Expected: {expected_type}.                          |
        |------------------------------------------------------|"""
        raise Exception(error_mensade)

    # parser
    def parse_program(self):
        statements = []
        while not self.is_at_end():
            stmt = self.parse_stmt()
            if stmt:
                statements.append(stmt)
        return statements

    # type of token parse
    def parse_stmt(self):
        t = self.peek()

        if t.type == TokenType.LET:
            return self.parse_var_declaration()

        self.consume(None, "Início de instrução inválido")

    # tokens parse
    def parse_var_declaration(self):
        self.advance()

        # var name
        name_token = self.consume(TokenType.IDENTIFIER, "Expected var name after 'let'")
        name = name_token.value

        # COLON symbol
        self.consume(TokenType.COLON, "Expected ':' after var name")

        # var type
        type_token = self.consume(TokenType.IDENTIFIER, "Expected var type")
        var_type = TypeNode(name=type_token.value)

        # ASSIGN symbol
        self.consume(TokenType.ASSIGN, "Expected '=' to initialize variable")

        # var value
        # todo: call parse_expression()
        value_token = self.consume(TokenType.NUMBER, "Expected numeric value")
        value = IntLiteral(value=int(value_token.value))

        return VarDeclaration(name=name, var_type=var_type, value=value)

    def parse_function_declaration(self):
        pass
    def parse_return_statement(self):
        pass


