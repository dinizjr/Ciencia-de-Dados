
'''Escreva uma função que receba três parâmetros (a,b e c) interiros e retorne o maior
valor entre os argumentos passados.'''

def trazer_maior(a,b,c):
    if(a > b and a > c):
        print(a)
    elif(b > a and b > c):
        print(b)
    else:
        print(c)

trazer_maior(10,8,20)

  #ou

'''def max(a,b,c):
    if a<b:
        if b<c:
            return c
        else:
            return b
        if a<b:'''











