import csv

class Customer(object):
    def __init__(self, id, name, gender, birthday, email, active):
        self.id = id
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.email = email
        self.active = active

def open_file(input_file):

    listcust = []
    actives = []

    with open(input_file, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)

        for row in reader:
            listcust.append(Customer(row[0], row[1], row[2], row[3], row[4], row[5]))

    for line in listcust:
        #print(line.active)
        if line.active == 'True':
            actives.append(line)

    print(len(actives))

open_file('D:/Documentos/Python/customers.csv')

