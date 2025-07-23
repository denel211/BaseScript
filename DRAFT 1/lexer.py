def tokenize(code):
    for ch in ['log', 'var', '(', ')', '[', ']', ';', '+', '*', '/', '-']:
        code = code.replace(ch, f'~{ch}~')
    tokens = [t for t in code.split('~') if t != '']
    for token in tokens:
        if token == " ":
            tokens.remove(" ")
    return tokens