from lexer import Lexer
from parser import Parser

def load_source(path: str) -> str:
    with open(path, 'r') as file:
        return file.read()


def debug_lexer(tokens):
    print("# LEXER DEBUG #")
    print(f"{'TIPO':<15} | {'VALOR':<15} | {'LINHA':<5} | {'COLUNA':<5}")
    print("-" * 50)
    for token in tokens:
        print(f"{token.type.name:<15} | {repr(token.value):<15} | {token.line:<5} | {token.column:<5}")


def debug_parser(node, indent=0):
    prefix = "  " * indent + "|-- "

    if isinstance(node, list):
        for item in node:
            debug_parser(item, indent)

    elif node.__class__.__name__ == "VarDeclaration":
        print(f"{prefix}VarDeclaration: {node.name}")
        debug_parser(node.var_type, indent + 1)
        debug_parser(node.value, indent + 1)

    elif node.__class__.__name__ == "TypeNode":
        print(f"{prefix}Type: {node.name}")

    elif node.__class__.__name__ == "IntLiteral":
        print(f"{prefix}IntLiteral: {node.value}")

    elif node.__class__.__name__ == "Identifier":
        print(f"{prefix}Identifier: {node.name}")

    elif node.__class__.__name__ == "BinaryExpr":
        print(f"{prefix}BinaryExpr ({node.operator})")
        debug_parser(node.left, indent + 1)
        debug_parser(node.right, indent + 1)

    else:
        print(f"{prefix}Unknown Node: {node}")

if __name__ == "__main__":
    try:
        path = "tests/lang02.txt"
        source_code = load_source(path)

        lexer = Lexer(source_code)
        tokens = lexer.tokenize
        debug_lexer(tokens)

        parser = Parser(tokens)
        ast = parser.parse_program()
        print("\n# PARSER DEBUG #")
        debug_parser(ast)

    except FileNotFoundError:
        print(f"Erro: {path} not found.")
    except Exception as e:
        print(f"Error: {e}")