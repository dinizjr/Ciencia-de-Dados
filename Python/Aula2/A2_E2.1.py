import csv
male = []
f = csv.DictReader(open('C:/Users/183134/Documents/Ciência de Dados/Python/heroes_information.csv'))
for row in f:
    if row['Gender'] == 'Male':
        print (row)
