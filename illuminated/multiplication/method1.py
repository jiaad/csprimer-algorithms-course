def recIntMult(x,y):
    n = len(str(x))
    if n == 1: return x * y
    two = (10 ** (n // 2))
    a = x //  two
    b = x % two
    c = y //two
    d = y % two
    print(a,b,c,d)
    ac = recIntMult(a, c)
    ad = recIntMult(a,d)
    bc = recIntMult(b,c)
    bd = recIntMult(b,d)
    print(ac, ad, bc, bd)
    print(ac, ad, bc, bd)
    return (10 ** n) * ac + (10 ** (n // 2)) * (ad + bc) + bd

print(recIntMult(5678, 1234))
