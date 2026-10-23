'''1) Dado um número inteiro e positivo, crie uma função que receberá esse número como argumento e retornará True
caso seja um número primo ou "Não é primo" caso contrário. O valor máximo que a função calculará é de 5,5 * 10^7.
Caso o número passado como argumento seja maior, retornar a mensagem "Número fora do range".'''

def num_primo(num):
    div = 0
    i = 1
    if num > 5.5*10**7:
        return "Número fora do range"
    else:
     while i <= num:
        if num % i == 0:
            div += 1
        i += 1

     if div == 2:
        return True
     else:
        return "Não é primo"


print(num_primo(55000005))

'''Enquanto o i for menor que o num divida num por i, se sobrar 0 coloca 1 em div, 
se no final o div der 2 quer dizer que só tem 2 divisores, o 1 e ele mesmo, ai é primo, 
se der maior que 2 tem mais divisores ai não é primo'''