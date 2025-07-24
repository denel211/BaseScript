import sys

import lexer
import parser
import interpreter
from debug import *
import time

def shell():
    printAnyways("=" * 39)
    printAnyways("         BaseScript by Daniel    ")
    printAnyways("          Version 1.4 - 2025        ")
    printAnyways("=" * 39)
    printAnyways("Welcome to the BaseScript Shell!")
    printAnyways("Type your commands below:")
    printAnyways("")

    while True:
        try:
            user_input = input(">>> ")
            tokenized = lexer.tokenize(user_input)
            parsed = parser.parse(tokenized)
            interpreter.run(parsed)
        except KeyboardInterrupt:
            printAnyways("\nExiting BaseScript Shell. Goodbye!")
            break
        except Exception as e:
            printAnyways(f"Error: {e}")


if len(sys.argv) > 1:
    if len(sys.argv) > 2:
        if sys.argv[2].startswith("build="):
            interpreter.build = sys.argv[2][6:]
    with open(sys.argv[1], "r", encoding="utf-8") as file:
        content = file.read().replace('\n', '').strip()
        tokenized = lexer.tokenize(content)
        parsed = parser.parse(tokenized)
        interpreter.run(parsed)
else:
    shell()