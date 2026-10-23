try:
    f = open('C:/Users/183134/Documents/Ciência de Dados/Python/teste.txt')
except FileNotFoundError as err:
    print('Arquivo não encontrado')
    print(err)
    exit(-1)
finally:
    print('Finalizado')
for line in f:
    print (line)