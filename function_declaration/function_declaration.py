import ply.lex as lex
import ply.yacc as yacc

# Define the tokens
tokens = (
    "DEF",
    "IDENTIFIER",
    "LPAREN",
    "RPAREN",
    "COMMA",
    "COLON",
)

# Token definitions
t_DEF = r"def"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_COMMA = r","
t_COLON = r":"
t_ignore = " \t\n"

reserved = {"def": "DEF"}

def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, "IDENTIFIER")
    return t

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser rules
def p_function_declaration(p):
    "function_declaration : DEF IDENTIFIER LPAREN params RPAREN COLON"
    print(f"Valid function declaration: {p[2]} with parameters {p[4]}")

def p_params(p):
    """params : param
              | params COMMA param
              | empty"""
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 4:
        p[0] = p[1] + [p[3]]

def p_param(p):
    "param : IDENTIFIER"
    p[0] = p[1]

def p_empty(p):
    "empty :"
    p[0] = []

def p_error(p):
    print("Syntax error in function declaration!")
    if p:
        print(f"Unexpected token: {p.type} - {p.value}")
    else:
        print("Unexpected end of input!")

parser = yacc.yacc()

def main():
    code = input("Enter a Python function declaration: ")
    result = parser.parse(code, lexer=lexer)
    if result:
        print("Parsing successful.")

if __name__ == "__main__":
    main()

