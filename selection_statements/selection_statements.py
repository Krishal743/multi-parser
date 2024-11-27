import ply.lex as lex
import ply.yacc as yacc

# Define the tokens
tokens = (
    "IF",
    "ELSE",
    "LPAREN",
    "RPAREN",
    "IDENTIFIER",
    "REL_OP",
    "SEMICOLON",
    "NUMBER",
    "EQUALS"
)

# Reserved keywords
reserved = {"if": "IF", "else": "ELSE"}

# Token definitions
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_REL_OP = r"(==|!=|<=|>=|<|>)"
t_SEMICOLON = r";"
t_EQUALS = r"="
t_ignore = " \t\n"

def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, "IDENTIFIER")
    return t

def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_error(t):
    t.lexer.skip(1)

# Initialize the lexer
lexer = lex.lex()

# Parsing rules
def p_selection_statement(p):
    """selection_statement : IF LPAREN condition RPAREN statement ELSE statement
                           | IF LPAREN condition RPAREN statement"""
    if len(p) == 6:
        print(f"Valid if statement with condition: {p[3]}")
    else:
        print(f"Valid if-else statement with condition: {p[3]}")

def p_condition(p):
    """condition : IDENTIFIER REL_OP IDENTIFIER
                 | IDENTIFIER REL_OP NUMBER"""
    p[0] = f"{p[1]} {p[2]} {p[3]}"

def p_statement(p):
    "statement : IDENTIFIER EQUALS IDENTIFIER SEMICOLON"
    p[0] = f"{p[1]} = {p[3]};"

def p_error(p):
    print("Syntax error in selection statement!")
    if p:
        print(f"Unexpected token: {p.type} - {p.value}")
    else:
        print("Unexpected end of input!")

# Initialize the parser
parser = yacc.yacc()

# Testing the parser
if __name__ == "__main__":
    code = "if (x > y) x = y: else x = z;"  # Example C++ selection statement
    result = parser.parse(code, lexer=lexer)
    if result is None:
        print("Parsing completed with no errors.")
def main():
    code = "if (x > 0) { y = 10; }"
    print(f"\nParsing Selection Statement: {code}")
    lexer.input(code)
    result = parser.parse(code, lexer=lexer)
    if result is None:
        print("Parsing completed with no errors.")

