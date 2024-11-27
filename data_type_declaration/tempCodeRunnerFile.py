import ply.lex as lex
import ply.yacc as yacc

# Define the tokens
tokens = (
    "DATATYPE",
    "IDENTIFIER",
    "SEMICOLON",
)

# Token definitions
t_SEMICOLON = r";"
t_ignore = " \t\n"

# Reserved words for C++ data types
reserved = {
    "int": "DATATYPE",
    "float": "DATATYPE",
    "double": "DATATYPE",
    "char": "DATATYPE",
}

def t_DATATYPE(t):
    r"int|float|double|char"
    return t

def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    return t

def t_error(t):
    t.lexer.skip(1)

# Initialize the lexer
lexer = lex.lex()

# Parsing rules
def p_datatype_declaration(p):
    "datatype_declaration : DATATYPE IDENTIFIER SEMICOLON"
    print(f"Valid data type declaration: {p[1]} {p[2]}")

def p_error(p):
    print("Syntax error in data type declaration!")
    if p:
        print(f"Unexpected token: {p.type} - {p.value}")
    else:
        print("Unexpected end of input!")

# Initialize the parser
parser = yacc.yacc()

# Testing the parser
if __name__ == "__main__":
    code = "int a;"  # Example C++ data type declaration
    result = parser.parse(code, lexer=lexer)
    if result is None:
        print("Parsing completed with no errors.")

def main():
    code = "int a;"
    print(f"\nParsing Data Type Declaration: {code}")
    lexer.input(code)
    result = parser.parse(code, lexer=lexer)
    if result is None:
        print("Parsing completed with no errors.")
