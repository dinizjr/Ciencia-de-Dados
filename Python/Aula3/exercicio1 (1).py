def f(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return 2 * f(n -1) + g(n -2)

def g(n):
    if n < 3:
        return n
    else:
        return g(n -1) + 3 * f(n -2)

def k(n):
    if(n > 0):
        return f(n), g(n)


print([k(i) for i in range(1, 6)])
exp = (k(i) for i in range(1, 6))
for i in exp:
    print(i)