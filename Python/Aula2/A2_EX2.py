import csv
def read_file(file:):
    f = open(file, 'r')
    male = []
    female = []
    indefined = []
    with open('C:/Users/183134/Documents/Ciência de Dados/Python/heroes_information.csv', 'rb') as arq:
        reader = csv.reader(arq)
    for line in reader:
        return (line)
print(read_file('C:/Users/183134/Documents/Ciência de Dados/Python/heroes_information.csv'))



