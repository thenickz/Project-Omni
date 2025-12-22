from enum import Enum, auto
from dataclasses import dataclass


class TokenType(Enum):
    _ = auto()
    # keywords
    FN = auto()
    RETURN = auto()
    LET = auto()
    CONST = auto()

    # identifier and types
    IDENTIFIER = auto()
    NUMBER = auto()

    # symbols
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    COLON = auto()
    COMMA = auto()
    ASSIGN = auto()
    ARROW = auto()
    PLUS = auto()
    MINUS = auto()

    EOF = auto()


@dataclass
class Token:
    type: TokenType
    value: str
    line: int
    column: int
