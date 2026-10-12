# Lexer for Custom Programming Language
keywords = {
    "let": "KEYWORD_LET",
    "print": "KEYWORD_PRINT",
    "if": "KEYWORD_IF",
    "else" : "KEYWORD_ELSE",
    "int": "KEYWORD_INT"
}

operators = {
    "=": "ASSIGN",
    "+": "PLUS",
    "-": "MINUS",
    "*": "MULTIPLY",
    "/": "DIVIDE",
    "<": "LESS_THAN",
    ">": "GREATER_THAN"
}

delimiters = {
    "{": "LEFT_BRACE",
    "}": "RIGHT_BRACE",
    "(": "LEFT_PAREN",
    ")": "RIGHT_PAREN",
    ";": "SEMICOLON"
}

def lexer(source_code):
    tokens = []
    i = 0
    while i < len(source_code):
        # 1. Whitespace -> ignore
        if source_code[i].isspace():
            i += 1
            continue

        # 2. String
        if source_code[i] == '"':
            start = i
            i += 1
            while i < len(source_code) and source_code[i] != '"':
                i += 1

            if i >= len(source_code):
                tokens.append(("ERROR", "Unterminated string"))
                break

            i += 1

            lexeme = source_code[start:i]
            tokens.append(("STRING", lexeme))
            continue

        # 3. Identifier or Keyword
        if source_code[i].isalpha():

            start = i
            i += 1

            # letter (letter | digit)*
            while i < len(source_code) and source_code[i].isalnum():
                i += 1

            lexeme = source_code[start:i]

            if lexeme in keywords:
                tokens.append((keywords[lexeme], lexeme))
            else:
                tokens.append(("IDENTIFIER", lexeme))

            continue

        # 4. Number
        if source_code[i].isdigit():

            start = i
            i += 1

            # digit+
            while i < len(source_code) and source_code[i].isdigit():
                i += 1

            lexeme = source_code[start:i]
            tokens.append(("NUMBER", lexeme))
            continue

        # 5. Operator
        if source_code[i] in operators:

            lexeme = source_code[i]
            tokens.append((operators[lexeme], lexeme))

            i += 1
            continue

        # 6. Delimiter
        if source_code[i] in delimiters:

            lexeme = source_code[i]
            tokens.append((delimiters[lexeme], lexeme))

            i += 1
            continue

        # 7. Invalid character
        tokens.append(("ERROR", source_code[i]))
        i += 1

    return tokens


# Take source code from user

print("=== CUSTOM LANGUAGE LEXER ===")
print("Enter your source code:")
print("Type done when finished (on a new line).")
print()

source_lines = []

while True:

    line = input()

    if line == "done":
        break

    source_lines.append(line)

source_code = "\n".join(source_lines)

# Run lexer
tokens = lexer(source_code)

# Display Token Table

print("\nTOKEN TABLE")
print("-" * 10)
print(f"{'Lexeme':<10} Token")
print("-" * 10)

for token, lexeme in tokens:
    print(f"{lexeme:<10} {token}")

print("-" * 10)
print("Total Tokens:", len(tokens))
    