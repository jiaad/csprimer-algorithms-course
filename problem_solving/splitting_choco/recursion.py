def split_choco(h, w):
    if w == 1: return h - 1
    else: return 1 + split_choco(h, w - 1) + split_choco(h, 1)

print(split_choco(1, 1))
print(split_choco(4, 3))
print(split_choco(8, 5))
print(split_choco(20, 5))
print(split_choco(30, 3))
