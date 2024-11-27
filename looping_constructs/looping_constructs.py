import ply.lex as lex
import ply.yacc as yacc

# Define tokens for C++ loop syntax
tokens = (
    "FOR",
    "WHILE",
    "LPAREN",
    "RPAREN",
    "SEMICOLON",
    "IDENTIFIER",
    "NUMBER",
    "ASSIGN",
    "LT",
    "GT",
    "PLUS",
    "MINUS",
)

# Regular expressions for tokens
t_FOR = r"for"
t_WHILE = r"while"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_SEMICOLON = r";"
t_ASSIGN = r"="
t_LT = r"<"
t_GT = r">"
t_PLUS = r"\+"
t_MINUS = r"-"
t_ignore = " \t"


# Identifier and number patterns

reserved = {"for": "FOR", "while": "WHILE"}


def t_IDENTIFIER(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, "IDENTIFIER")
    return t


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


# Initialize lexer
lexer = lex.lex()


# Parsing rules for C++ loops
def p_loop_statement(p):
    """loop_statement : for_loop
    | while_loop"""
    pass


def p_for_loop(p):
    """for_loop : FOR LPAREN assignment SEMICOLON condition SEMICOLON assignment RPAREN SEMICOLON"""
    print(
        f"Valid for loop with initialization: {p[3]}, condition: {p[5]}, and update: {p[7]}"
    )


def p_while_loop(p):
    """while_loop : WHILE LPAREN condition RPAREN SEMICOLON"""
    print(f"Valid while loop with condition: {p[3]}")


# Assignment expressions
def p_assignment(p):
    "assignment : IDENTIFIER ASSIGN expression"
    p[0] = f"{p[1]} = {p[3]}"


# Condition expressions
def p_condition(p):
    """condition : expression LT expression
    | expression GT expression"""
    p[0] = f"{p[1]} {p[2]} {p[3]}"


# Arithmetic expressions
def p_expression(p):
    """expression : IDENTIFIER
    | NUMBER
    | expression PLUS expression
    | expression MINUS expression"""
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = f"{p[1]} {p[2]} {p[3]}"


# Error handling in parsing
def p_error(p):
    print("Syntax error in loop statement!")
    if p:
        print(
            f"Syntax error at line {p.lineno}, position {p.lexpos}, token {p.type}, value {p.value}"
        )
    else:
        print("Unexpected end of input!")


# Initialize parser
parser = yacc.yacc()

# Sample main function to run the parser
if __name__ == "__main__":
    # Example code snippets for C++ style loops
    code_for = "for (i = 0; i < 10; i = i + 1);"
    code_while = "while (x > 0);"

    # Parsing the for loop
    print("Parsing for loop:")
    result_for = parser.parse(code_for, lexer=lexer)

    # # Parsing the while loop
    print("\nParsing while loop:")
    result_while = parser.parse(code_while, lexer=lexer)