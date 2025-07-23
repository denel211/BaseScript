import sys
from debug import *

build = False
scope = {}

def number(string):
    if string.startswith('"'):
        return string[1:-1]
    
    return string

def get_string(expression):
    # printAnyways(expression)
    match expression['type']:
        case "binary_expression":
            # printAnyways(f"{expression['left']} {expression['operator']} {expression['right']}")
            return f"{expression['left']} {expression['operator']} {expression['right']}"
        case "string":
            return f"\"{expression['value']}\""
        case "number":
            return str(expression['value'])
        case "variable":
            return expression['value']
        case "input":
            data = f"\"{input(expression['value'][1:-1])}\""
            # printAnyways("DATA: ", data)
            return data
        case "string_addition":
            totalString = ""
            for token in expression['tokens']:
                totalString = totalString + " str(" + str(token) + ") + "
            # totalString = "".join(f"str({str(expression['tokens'])})")
            # print("TOTAL STRING: ", totalString)
            return totalString[:-3]
        case "bool_expression":
            print("BOOL EXPRESSION")
            print("-----EXPRESSION-----")
            print(expression)
            print("-----EXPRESSION-----")
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
                print("LT OPERATOR")
                operator = "<"
                print(f"{expression['left']} {operator} {expression['right']}")
                return f"int({number(expression['left'])}) {operator} int({number(expression['right'])})"

def run(parsed):
    pythonActions = []

    for action in parsed:
        def interpret_action(action, indent=0):
            indent_str = "  " * indent
            match action['type']:
                case "variable_declaration":
                    print(action)
                    return f"{indent_str}{action['name']} = {get_string(action['value'])}"
                case "print_statement":
                    printAnyways(action)
                    return f"{indent_str}print({get_string(action['value'])})"
                case "input_statement":
                    return f"{indent_str}input({get_string(action['value'])})"
                case "if_statement":
                    # ifAction = action['action']
                    # ifActionInterpreted = interpret_action(ifAction, indent + 1)
                    # return f"{indent_str}if {get_string(action['bool_expression'])}:\n{ifActionInterpreted}"
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
        
        pythonActions.append(interpret_action(action))
    
    lines = []
    for action in pythonActions:
        lines.append(action)
    code = "\n".join(lines)
    print(code)
    if build == False: exec(code, {}, scope)
    if build != False:
        with open(build, "w", encoding="utf-8") as file:
	        file.write(code)
