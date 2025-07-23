def split_statements(tokens):
    statements = []
    current = []
    for token in tokens:
        if token == ";":
            if current:
                statements.append(current)
                current = []
        else:
            current.append(token)
    if current:
        statements.append(current)
    return statements

def parse_expression(tokens):
    print("PARSING EXPRESSION: ", tokens)
    if len(tokens) == 1:
        token = tokens[0][1:]
        print(token)
        if token.isdigit():
            return {"type": "number", "value": int(token)}
        elif token.startswith('"') and token.endswith('"'):
            return {"type": "string", "value": token.strip('"')}
        else:
            return {"type": "variable", "value": token}
    
    if len(tokens) == 3:
        left = parse_expression([tokens[0]])
        operator = tokens[1]
        right = parse_expression([tokens[2]])
        print(left, operator, right)
        if operator.replace(" ", "") in ["+", "-", "*", "/"]:
            return {
                "type": "binary_expression",
                "operator": operator,
                "left": left,
                "right": right
            }
    return {"type": "unknown", "tokens": tokens}


def parse_statement(tokens):
    if tokens[0] == "log":
        expr = parse_expression(tokens[1:])
        return {"type": "print_statement", "value": expr}

def parse(tokens):
    parsed = []
    statements = split_statements(tokens)
    for stmt_tokens in statements:
        parsed_stmt = parse_statement(stmt_tokens)
        if parsed_stmt is not None:
            parsed.append(parsed_stmt)
    return parsed
