'''Crie uma função que encontre um caracter dentro de uma frase.
Caso encontre, deverá retornar a posição desse caracter, caso contrário -1. (Não usar o operador IN)'''

def encontre_a_letra(str,ch):
    indice = 0
    while indice < len(str):
        if str[indice] == ch:
            return indice
        indice += 1
    return -1
print(encontre_a_letra("paralelepípedo","a"))