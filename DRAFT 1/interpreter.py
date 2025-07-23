scope = {}

def run(parsed):
    # print(parsed)
    pythonActions = []
    for action in parsed:
        if action['type'] == "print_statement":
            printValue = ""
            dontAppend = False
            if action['value']['type'] == "binary_expression":
                left = action['value']['left']
                operator = action['value']['operator']
                right = action['value']['right']
                printValue = str(eval(f"{left} {operator} {right}"))
            if action['value']['type'] == "string":
                printValue = action['value']['value']
            if action['value']['type'] == "variable":
                printValue = str(action['value']['value'])
                pythonActions.append(f"print({printValue})")
                dontAppend = True
            if not dontAppend: pythonActions.append(f"print(\"{printValue}\")")
        if action['type'] == "variable_declaration":
            varValue = ""
            varName = ""
            if action['value']['type'] == "binary_expression":
                left = action['value']['left']
                operator = action['value']['operator']
                right = action['value']['right']
                # print(str(eval(f"{left} {operator} {right}")))
                varValue = str(eval(f"{left} {operator} {right}"))
                varName = action['value']['variable']
            # print(action['value']['type'])
            if action['value']['type'] == "string":
                varValue = action['value']['value'].split()[0]
                varName = action['value']['value'].split()[0]
            # print(action['value'])
            pythonActions.append(f"{varName} = {varValue}")
    for action in pythonActions:
        print(action)
        # exec(action, {}, scope)