from lexer import Lexer


def load_source(path: str) -> str:
    with open(path, 'r') as file:
        return file.read()


def debug_lexer(tokens):
    print(f"{'TIPO':<15} | {'VALOR':<15} | {'LINHA':<5} | {'COLUNA':<5}")
    print("-" * 50)
    for token in tokens:
        print(f"{token.type.name:<15} | {repr(token.value):<15} | {token.line:<5} | {token.column:<5}")


if __name__ == "__main__":
    try:
        path = "dev/lang01.txt"
        source_code = load_source(path)

        lexer = Lexer(source_code)

        tokens = lexer.tokenize

        debug_lexer(tokens)

    except FileNotFoundError:
        print(f"Erro: {path} not found.")
    except Exception as e:
        print(f"Error: {e}")