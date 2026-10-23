def F(n):

    if n == 1:
        return 2
    elif n == 2:
        return 1
    elif n >= 3:
        return 2 * F(n - 1) + G(n - 2)

def G(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n >= 3:
        return G(n - 1) + 3 * F(n - 2)

def K(n):
    if n > 0:
    return (F(n), G(n))
print(K(4))



'''def G(n):
    if n < 3:
        return n
    else:
        return G(n - 1) + 3 * F(n - 2)'''

print([K(i) for i in rsnge(1,6)])

exp = (K(i) for i in rsnge(1,6))
for i in exp:
    print (i)



