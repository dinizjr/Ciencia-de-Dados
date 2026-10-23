'''Crie uma função que receba duas listas numéricas, retorne a soma dos produtos de elementos de mesmo indice de cada lista.
Caso uma das listas tenha mais elementos que a outra, considere o valor 1 para o produto com cada elemento da lista com maior
número de elementos. Caso as duas listas estejam vazias, retornar -1.'''

def soma_listas(a,b):
    x = len(a)
    y = len(b)
    list = []
    if (x == 0 and y == 0):
        return -1
    if x > y:
        while y < x:
            b.append(1)
            y += 1
    else:
        while x < y:
            a.append(1)
            x += 1
    for index in range(x):
        list.append(a[index] + b[index])
    return list
print(soma_listas([5,2,6],[4,2,6,5]))