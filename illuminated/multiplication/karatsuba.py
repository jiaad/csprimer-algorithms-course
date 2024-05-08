def karatsuba(x, y):
    n = max(len(str(x)), len(str(y)))
    if n == 1: return x * y
    two = (10 ** (n // 2)) 
    
    a = x // two
    b = x % two 
    c = y // two 
    d = y % two 
    p = a + b
    q = c + d

    ac = karatsuba(a, c)
    bd = karatsuba(b, d) 
    pq = karatsuba(p, q)
    adbc = (pq - ac - bd)
    return (10 ** n) + (10 ** (n // 2)) * (adbc + (b * d))

print(karatsuba(5678, 1234))
