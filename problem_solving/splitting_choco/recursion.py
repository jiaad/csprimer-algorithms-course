def split_choco(h, w):
    if w == 1: return h - 1
    else: return 1 + split_choco(h, w - 1) + split_choco(h, 1)

print(split_choco(4, 3))
