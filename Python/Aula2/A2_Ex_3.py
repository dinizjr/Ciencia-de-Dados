import csv
#def process_file(filename):
    # open input file for reading
    input_file = open(filename, 'r')

    y = 'Year'
    anos = []
    reader = csv.reader(input_file)
    next(reader)

    for row in f:
        if row[0][3:4] == 0:
            print (row)


   # print (row)
#process_file('C:/Users/183134/Documents/Ciência de Dados/Python/WorldCups.csv')