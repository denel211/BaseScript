debug = False

def dummyPrint(a="", b="", c="", d="", e="", f="", g="", h=""):
    pass

def printAnyways(a="", b="", c="", d="", e="", f="", g="", h=""):
    pass

printAnyways = print
if not debug: print = dummyPrint