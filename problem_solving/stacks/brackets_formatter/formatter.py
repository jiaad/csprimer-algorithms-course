s = """
{
  {
            {
            
      }

      }
}
"""

class Data(object):
  def __init__(self, line, pos, ch) -> None:
    self.line = line
    self.pos = pos
    self.ch = ch

stack = []

def line(s, l):
    ls = [] 
    if len(s) == 0: return
    for pos, x in enumerate(s):
      if x in (" ", "\n", ""):
        ls.append(x)
      elif x == "{":
        ls.append(x)
        stack.append(Data(l, pos, x))
      else:
        left = stack.pop()
        if left.pos == pos:
          ls.append("}")
        elif left.pos > len(ls):
          while len(ls) <= left.pos:
            ls.append(" ")
          ls[left.pos] = "}"
        else:
          ls[left.pos] = "}"
    print("".join(ls))


def format(s):
  s = s.split("\n")
  for n, x in enumerate(s):
    line(x, n)
    print("\n", end="")


print("input")
print(s)
print("=========================================")
print("output")
format(s)