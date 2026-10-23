'''Escreva uma função que receba uma lista de números e retorne uma tupla com duas listas,a primeira contendo
todos os números pares e a segunda contendo todos os números ímpares ordenados'''

def separa_par_impar(a):
    par = []
    impar = []
    a.sort()
    for item in a:
        if (item % 2 == 0): #divide o número por 2, se não sobrar resto é par ,se sobrar é impar
            par.append(item)
        else:
            impar.append(item)

    return(par,impar)

print(separa_par_impar([1,5,2,8,6,8,2,0,21,32,4,8,9,2,1,54,75,2,3,0]))