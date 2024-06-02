def exp(a, n):
  if n == 0: return 1
  if n == 1: return a
  res = exp(a , n >> 1)
  if n & 1: return res * a * res
  return res * res

def exp_itter(a, n):
  res = 1
  while n > 0:
    if n & 1: 
      res *= a
    a = a * a
    n = n >> 1
  return res

print(exp(2, 10 ))
print(exp_itter(2, 10 ))


def three(a, n):
  res = 1
  while n:
    if n & 1: 
      res = res * a
    a = a * a
    n = n >> 1
  return a
print(three(2, 16))
# print(three(2, 10))
# print(exp(2, 11))
# print(exp(2, 12))
# print(exp(2, 13))
# for 3, 10  (3 + 3 + 9+ 3 + 3 + 9 + 81) * 90 * 6