from debug import *
import re

functiontokens = ['log', 'var', 'input', 'if', 'repeat']
statictokens = ['(', ')', '[', ']', '{', '}', ';', '+', '*', '/', '-', '=', ':']

token_patterns = functiontokens + statictokens

token_regex = re.compile(r'("([^"\\\\]|\\\\.)*")|' + r'(' + '|'.join(re.escape(tok) for tok in token_patterns) + r')|' + r'([A-Za-z_][A-Za-z0-9_]*)|' + r'(\d+)|' + r'(\S)')

def tokenize(code):
    tokens = []
    pos = 0
    while pos < len(code):
        match = token_regex.match(code, pos)
        if not match:
            if code[pos].isspace():
                pos += 1
                continue
            else:
                raise ValueError(f"Unexpected character: {code[pos]}")
        token = match.group(0)
        tokens.append(token)
        pos = match.end()
    tokens = [t for t in tokens if not t.isspace()]
    return tokens
