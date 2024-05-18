PARENS = ["(", ")", "[", "]", "{", "}"]
PAR_DICT = {")": "(", "]":"[", "}":"{"}
CLOSED_PAR = [")", "]", "}"]


def rkt_paren_match(file):
    stack = []
    with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
               lint(line, stack)

def lint(line, stack):
    if not line.startswith(";"):
       return paren_match(line, stack)
    return []

def paren_match(line, stack):
    for i, x in enumerate(line, 1):
        if len(stack) == 0: 
            stack.append(x)
        elif x in PARENS:
            last = stack[-1]
            if x in CLOSED_PAR:
                if PAR_DICT.get(x, 0) != last: error(x, i, last, line)
                else: stack.pop()
            else: stack.append(x)
    return stack


def error(elem, pos, last, line):
    inversed = {"(": ")", "[": "]","{": "}"}
    print("syntax error", "char:",elem, "pos:", pos, "expected:", inversed.get(last, 0), "line:",line.strip())

# rkt_paren_match("./stretch.rkt")
#print(paren_match("[][][]", []))
rkt_paren_match("./stretch.rkt")
rkt_paren_match("./js.js")
#print(paren_match("[][][]", []))
