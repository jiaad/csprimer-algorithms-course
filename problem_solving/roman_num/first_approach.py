def int_to_r(num):
    lows = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousands = ["M", "MM", "MMM"]
    
    res = ""
    idx = 0
    if num >= 1000:
        idx = num // 1000
        num = num - 1000 * idx
        res += thousands[idx - 1]
    if num >= 100:
        idx = num // 100
        num = num - 100 * idx
        res += hundreds[idx - 1]
    if num >= 10:
        idx = num // 10
        num = num - (10 * idx)
        res += tens[idx - 1]
    if num >= 1:
        res += lows[num - 1]
    return res

romans = ["IX", "X", "XXI", "XXXIX", "CI", "CCXLVI", "DCCLXXXIX", "MMCDXXI"]
nums = [9, 10, 21, 39, 101, 246, 789, 2421]
for i, x in enumerate(nums):
    assert(int_to_r(x) == romans[i])
print("ok")
