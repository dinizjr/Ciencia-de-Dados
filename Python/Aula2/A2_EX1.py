nomes = []
tamanho = []
data = []
try:
    f = open('C:/Software Splice/Python/files.txt')
except FileNotFoundError as err:
    print('Arquivo não encontrado')
    print(err)
    exit(-1)
finally:
    print('Finalizado')
for line in f:
    #print(line)
    #nomes = print (line[0:6])
    if 'K' in (line[6:12]):
        tamanho = float(line[6:11])*1024
        print (tamanho)


