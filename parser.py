from debug import *

def split_statements(tokens):
    statements = []
    current = []
    brace_count = 0
    for token in tokens:
        if token == "{":
            brace_count += 1
            current.append(token)
        elif token == "}":
            brace_count -= 1
            current.append(token)
        elif token == ";" and brace_count == 0:
            if current:
                statements.append(current)
                current = []
            else:
                continue
        else:
            current.append(token)
    if current:
        statements.append(current)
    return statements

def parse_expression(tokens):
    if len(tokens) == 1 and len(tokens[0].split("__")) == 1:
        token = tokens[0]
        if token.isdigit():
            return {"type": "number", "value": int(token)}
        elif token.startswith('"') and token.endswith('"'):
            return {"type": "string", "value": token.strip('"')}
        elif token == "True" or token == "False":
            return {
                "type": "bool_expression",
                "value": token,
                "variable": tokens[0].split()[0] or ""
            }
        else:
            return {"type": "variable", "value": token}
    if len(tokens) == 2:
        if tokens[0] == "input":
            return {"type": "input", "value": tokens[1]}
    if len(tokens) == 3:
        left = tokens[0]
        operator = tokens[1]
        right = tokens[2]
        if operator in ["+", "-", "*", "/"]:
            return {
                "type": "binary_expression",
                "operator": operator,
                "left": left,
                "right": right,
                "value": "NIS",
                "variable": tokens[0].split()[0] or ""
            }
    if len(tokens) == 5:
        left = tokens[1]
        operator = tokens[2]
        right = tokens[3]
        if operator in ["is", "isnt", "gt", "lt"] and tokens[0] == "(" and tokens[-1] == ")":
            return {
                "type": "bool_expression",
                "operator": operator,
                "left": left,
                "right": right,
                "value": "NIS",
                "variable": tokens[0].split()[0] or ""
            }
    if len("".join(tokens).split("__")) != 1:
        returnTokens = []
        for token in "".join(tokens).split("__"):
            returnTokens.append(token.strip())
        return {"type": "string_addition", "tokens": returnTokens}

def parse_statement(tokens):
    if tokens[0] == "log":
        expr = parse_expression(tokens[1:])
        return {"type": "print_statement", "value": expr}
    if tokens[0] == "var":
        expr = parse_expression(tokens[3:])
        return {"type": "variable_declaration", "name": tokens[1], "value": expr}
    if tokens[0] == "input":
        expr = parse_expression(tokens[1:])
        return {"type": "input_statement", "value": expr}
    if tokens[0] == "if":
        colon_index = tokens.index(":")
        if colon_index + 1 < len(tokens) and tokens[colon_index + 1] == "{":
            block_tokens = []
            brace_count = 0
            for i in range(colon_index + 1, len(tokens)):
                if tokens[i] == "{":
                    brace_count += 1
                    if brace_count == 1:
                        continue
                if tokens[i] == "}":
                    brace_count -= 1
                    if brace_count == 0:
                        break
                if brace_count >= 1:
                    block_tokens.append(tokens[i])
            statements = []
            current = []
            for token in block_tokens:
                if token == ";":
                    if current:
                        statements.append(current)
                        current = []
                else:
                    current.append(token)
            if current:
                statements.append(current)
            actions = []
            for stmt in statements:
                parsed_stmt = parse_statement(stmt)
                if parsed_stmt is not None:
                    actions.append(parsed_stmt)
            expr = parse_expression(tokens[1:colon_index])
            return {"type": "if_statement", "amount_expression": expr, "actions": actions}
        else:
            expr = parse_expression(tokens[1:colon_index])
            return {"type": "if_statement", "amount_expression": expr, "action": parse_statement(tokens[colon_index+1:])}
    if tokens[0] == "repeat":
        colon_index = tokens.index(":")
        if colon_index + 1 < len(tokens) and tokens[colon_index + 1] == "{":
            block_tokens = []
            brace_count = 0
            for i in range(colon_index + 1, len(tokens)):
                if tokens[i] == "{":
                    brace_count += 1
                    if brace_count == 1:
                        continue
                if tokens[i] == "}":
                    brace_count -= 1
                    if brace_count == 0:
                        break
                if brace_count >= 1:
                    block_tokens.append(tokens[i])
            statements = []
            current = []
            for token in block_tokens:
                if token == ";":
                    if current:
                        statements.append(current)
                        current = []
                else:
                    current.append(token)
            if current:
                statements.append(current)
            actions = []
            for stmt in statements:
                parsed_stmt = parse_statement(stmt)
                if parsed_stmt is not None:
                    actions.append(parsed_stmt)
            expr = parse_expression(tokens[1:colon_index])
            return {"type": "repeat_statement", "amount_expression": expr, "actions": actions}
        else:
            expr = parse_expression(tokens[1:colon_index])
            return {"type": "repeat_statement", "amount_expression": expr, "action": parse_statement(tokens[colon_index+1:])}

def parse(tokens):
    parsed = []
    statements = split_statements(tokens)
    for stmt_tokens in statements:
        parsed_stmt = parse_statement(stmt_tokens)
        if parsed_stmt is not None:
            parsed.append(parsed_stmt)
    return parsed
