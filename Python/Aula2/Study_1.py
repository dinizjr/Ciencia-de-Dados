#ABRIR ARQUIVOS
def read_arq(file):
    f = open(file, 'r')
    #arq = []
    for line in f:
        print(line)
print(read_arq('C:/Software Splice/Python/heroes_information.csv'))