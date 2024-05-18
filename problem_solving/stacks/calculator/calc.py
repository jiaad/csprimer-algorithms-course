
OPS = {
  "+": lambda a, b: a + b,
  "-": lambda a, b: a - b
}

def calc(s):
  res , op = 0, ""
  for x in s:
    if x in ("(",")", " "): continue # fiter
    if x in ("+", "-"):
      op = x
      continue
    if op in ("+", "-"):
      res = OPS[op](res, int(x))
    else: res = int(x)
    op = ""
  return res

def calculator(s):
  temp, stack = [], []
  for x in s:
    if x == " ": continue
    stack.append(x)
    if x == ")":
      i = len(stack) - 1
      while stack[i] != "(":
        pop = stack.pop()
        if not pop in ("(",")"):
          temp.insert(0, pop)
        i -= 1
      stack.pop()
      stack.append(calc(temp))
      temp = []
  return int(stack.pop())

assert calculator("0") == 0
assert calculator("1") == 1

print(calculator("( 1 - (2 + 3 + (4 - 5)))"))
assert calculator("( 1 - (2 + 3 + (4 - 5)))") == -3
assert calculator("( 1 + (2 + 3 + (4 + 5)))") == 15
assert calculator("( 1 - (2 + 3 + (4 + 5)))") == -13
assert calculator("(1 + 3)") == 4
assert calculator("((1 + 2) + (3 + 4 - (1 + 2)))") == 7
assert calculator("((1+2 + (1 + 2 + (1 + 1) + (1 + 9 + (1 + 9))))") == 28
assert calculator("(2 - 1)") == 1
assert calculator("(2 + 1 + 2 + 2 + 2 + 2 + 2 + (1 + 1 + 1 + 1 + 1 + 1 + (1 + 1 + 1 + 1)))") == 23

# for expr, expected in [
#         ("(2-1)", 1),
#         ("(21-1)", 20),
#         ("(21-1*3)", 18),
#         ("(2-1*(2+3))", -3),
#         ("((1-1)*(2+3))", 0),
#         ("((5-1)/(1+1))", 2),
#         ("((5-1)/2)", 2),
#         ("(4/2/2)", 1),
#         ("(3*(2*(1)))", 6),
# ]:
#     assert calculator(expr) == expected, f"got {calc(expr)}, expected {expected}"

print("ok")

