import ply.lex as lex
import ply.yacc as yacc

# Define the tokens
tokens = (
    "LET",
    "IDENTIFIER",
    "LBRACKET",
    "RBRACKET",
    "SEMICOLON",
)

# Reserved keywords
reserved = {"let": "LET"}

# Token definitions
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_SEMICOLON = r";"
t_ignore = " \t\n"

def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, "IDENTIFIER")  # Check for reserved words
    return t

def t_error(t):
    t.lexer.skip(1)

# Initialize the lexer
lexer = lex.lex()

# Parsing rules
def p_array_declaration(p):
    "array_declaration : LET IDENTIFIER LBRACKET RBRACKET SEMICOLON"
    print(f"Valid array declaration: {p[2]}[]")

def p_error(p):
    print("Syntax error in array declaration!")
    if p:
        print(f"Unexpected token: {p.type} - {p.value}")
    else:
        print("Unexpected end of input!")

# Initialize the parser
parser = yacc.yacc()

# Testing the parser
if __name__ == "__main__":
    code = "let arr=[1,4,5];"  # Example JavaScript array declaration
    result = parser.parse(code, lexer=lexer)
    if result is None:
        print("Parsing completed with no errors.")



