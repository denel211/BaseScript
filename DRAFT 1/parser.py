# def print(a, b="", c="", d="", e=""):
#     pass

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
    # print(tokens)
    if len(tokens) == 1:
        token = tokens[0]
        if token.startswith(" "): token = tokens[0][1:]
        # print(token)
        if token.isdigit():
            return {"type": "number", "value": int(token)}
        elif token.startswith('"') and token.endswith('"'):
            return {"type": "string", "value": token.strip('"')}
        else:
            return {"type": "variable", "value": token}
    # print(tokens)
    if len(tokens) == 3:
        left = tokens[0][1:].split()[1]
        operator = tokens[1].replace(" ", "")
        right = tokens[2]
        if operator in ["+", "-", "*", "/"]:
            return {
                "type": "binary_expression",
                "operator": operator,
                "left": left,
                "right": right.replace(" ", ""),
                "variable": tokens[0][1:].split()[0] or ""
            }
    return {"type": "unknown", "tokens": tokens}


def parse_statement(tokens):
    if tokens[0] == "log":
        expr = parse_expression(tokens[1:])
        return {"type": "print_statement", "value": expr}
    if tokens[0] == "var":
        expr = parse_expression(tokens[1:])
        return {"type": "variable_declaration", "value": expr}

def parse(tokens):
    parsed = []
    statements = split_statements(tokens)
    for stmt_tokens in statements:
        parsed_stmt = parse_statement(stmt_tokens)
        if parsed_stmt is not None:
            parsed.append(parsed_stmt)
    return parsed
