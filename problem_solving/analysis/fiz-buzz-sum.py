def get_closest(n, div):
    return (n//div) * div

def sum_of_n(n, num):
    return ((n // num) * (n + num)) // 2

def sum_fiz_buzz(n):
    if n == 0: return 0
    three = get_closest(n, 3)
    five = get_closest(n, 5)
    fifteen = get_closest(n, 15)
    return (sum_of_n(three, 3) + sum_of_n(five, 5)) - sum_of_n(fifteen, 15)

assert sum_fiz_buzz(999) == 233168
assert sum_fiz_buzz(0) == 0
assert sum_fiz_buzz(3) == 3
assert sum_fiz_buzz(5) == 8
assert sum_fiz_buzz(6) == 14
assert sum_fiz_buzz(8) == 14
assert sum_fiz_buzz(9) == 23
assert sum_fiz_buzz(10) == 33
assert sum_fiz_buzz(12) == 45
assert sum_fiz_buzz(15) == 60
assert sum_fiz_buzz(18) == 78
assert sum_fiz_buzz(20) == 98
assert sum_fiz_buzz(21) == 119
assert sum_fiz_buzz(24) == 143
assert sum_fiz_buzz(25) == 168
print("ok")
print("ok")
