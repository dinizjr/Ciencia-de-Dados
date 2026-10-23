'''Dado um número inteiro não negativo(n), escreva duas funções sendo a primeira usando estruturas de repetição
FOR e a segunda usando estruturas de repetição WHILE, retornem o fatorial de n(n!)'''

def fatorial(a):
    x = 1
    for item in range(1,a + 1):
        x *= item
    return x
print(fatorial(3))


def fat(a):
    x = 1
    while (a > 1):
        x *= a
        a -= 1
    return x
print(fat(7))