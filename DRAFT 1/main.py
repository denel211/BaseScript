import sys

import lexer
import parser
import interpreter

def shell():
    while True:
        tokenized = lexer.tokenize(input(">>> "))
        interpreter.run(parser.parse(tokenized))

if len(sys.argv) > 1:
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        content = file.read().replace('\n', '').strip()
        tokenized = lexer.tokenize(content)
        # print(tokenized)
        interpreter.run(parser.parse(tokenized))
else:
    shell()