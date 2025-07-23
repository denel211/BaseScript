import sys
from debug import *

build = False
scope = {}

def number(string):
    if string.startswith('"'):
        return string[1:-1]
    
    return string

def get_string(expression):
    match expression['type']:
        case "binary_expression":
            return f"{expression['left']} {expression['operator']} {expression['right']}"
        case "string":
            return f"\"{expression['value']}\""
        case "number":
            return str(expression['value'])
        case "variable":
            return expression['value']
        case "input":
            data = f"input(\"{expression['value'][1:-1]}\")"
            return data
        case "string_addition":
            totalString = ""
            for token in expression['tokens']:
                totalString = totalString + " str(" + str(token) + ") + "
            return totalString[:-3]
        case "bool_expression":
            if expression["value"] != "NIS":
                return expression["value"]
            if expression['operator'] == "is":
                operator = "=="
                return f"{expression['left']} {operator} {expression['right']}"
            if expression['operator'] == "isnt":
                operator = "!="
                return f"{expression['left']} {operator} {expression['right']}"
            if expression['operator'] == "gt":
                operator = ">"
                return f"int({number(expression['left'])}) {operator} int({number(expression['right'])})"
            if expression['operator'] == "lt":
                operator = "<"
                return f"int({number(expression['left'])}) {operator} int({number(expression['right'])})"

def run(parsed):
    pythonActions = []

    for action in parsed:
        def interpret_action(action, indent=0):
            indent_str = "  " * indent
            match action['type']:
                case "variable_declaration":
                    return f"{indent_str}{action['name']} = {get_string(action['value'])}"
                case "print_statement":
                    return f"{indent_str}print({get_string(action['value'])})"
                case "input_statement":
                    return f"{indent_str}input({get_string(action['value'])})"
                case "if_statement":
                    amount_expr = get_string(action['amount_expression'])
                    if "actions" in action:
                        block_lines = []
                        for act in action['actions']:
                            interpreted = interpret_action(act, indent + 1)
                            indented_lines = "\n".join("  " + line if line.strip() != "" else line for line in interpreted.split("\n"))
                            block_lines.append(indented_lines)
                        block_code = "\n".join(block_lines)
                        return f"{indent_str}if {amount_expr}:\n{block_code}"
                    else:
                        repAction = action['action']
                        repActionInterpreted = interpret_action(repAction, indent + 1)
                        return f"{indent_str}if {amount_expr}:\n{block_code}"
                case "repeat_statement":
                    amount_expr = get_string(action['amount_expression'])
                    if "actions" in action:
                        block_lines = []
                        for act in action['actions']:
                            interpreted = interpret_action(act, indent + 1)
                            indented_lines = "\n".join("  " + line if line.strip() != "" else line for line in interpreted.split("\n"))
                            block_lines.append(indented_lines)
                        block_code = "\n".join(block_lines)
                        return f"{indent_str}for index in range(int({amount_expr})):\n{block_code}"
                    else:
                        repAction = action['action']
                        repActionInterpreted = interpret_action(repAction, indent + 1)
                        return f"{indent_str}for index in range(int({amount_expr})):\n{repActionInterpreted}"
                case "func_declaration":
                    amount_expr = action['name']
                    totalParamString = ",".join(action['params'])[2:]
                    if "actions" in action:
                        block_lines = []
                        for act in action['actions']:
                            interpreted = interpret_action(act, indent + 1)
                            indented_lines = "\n".join("  " + line if line.strip() != "" else line for line in interpreted.split("\n"))
                            block_lines.append(indented_lines)
                        block_code = "\n".join(block_lines)
                        return f"{indent_str}def {amount_expr}({totalParamString}):\n{block_code}"
                    else:
                        repAction = action['action']
                        repActionInterpreted = interpret_action(repAction, indent + 1)
                        return f"{indent_str}def {amount_expr}({totalParamString}):\n{repActionInterpreted}"
                case "func_call":
                    totalParamString = ""
                    for param in action['params']:
                        print(param)
                        totalParamString += get_string(param) + ","
                    return f"{indent_str}{action['name']}({totalParamString[:-1]})"
        
        pythonActions.append(interpret_action(action))
    
    lines = []
    for action in pythonActions:
        lines.append(action)
    code = "\n".join(lines)
    if build == False: exec(code, {}, scope)
    if build != False:
        with open(build, "w", encoding="utf-8") as file:
	        file.write(code)
