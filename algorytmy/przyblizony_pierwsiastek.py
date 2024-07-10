def pierw(P):
    eps = 0.0001
    a = 1
    b = P / a
    while abs(a-b) >= eps:
        a = (a + b) / 2
        b = P/a
    return (a + b) / 2

print(pierw(3))
