from enum import Enum, auto
from dataclasses import dataclass


class TokenType(Enum):
    _ = auto()
    # keywords
    ## statments
    RETURN = auto()

    ## declarations
    FN = auto()
    LET = auto()
    CONST = auto()
    # IF = auto()
    # ELSE = auto()
    # ELIF = auto()
    # WHILE = auto()
    # FOR = auto()
    # CLS = auto()

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
