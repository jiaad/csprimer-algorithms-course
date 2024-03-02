def int_to_roman(num):
    if num == 0:
        return ""
    else: return "x" + int_to_roman(num // 10)

print(int_to_roman(30))
