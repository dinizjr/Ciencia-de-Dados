'''Escreva uma função que receba dois valores inteiros positivos, e retorne a soma da sequência numérica inteira
entre o primeiro e o segundo parâmetro,inclusive.'''
def soma_seq(a,b):
    x = 0
    if a < b:
        for item in range(a,b + 1):
            x += item
    else:
        for item in range(b,a + 1):
            x += item
    return x
print(soma_seq(6,5))
