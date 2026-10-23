import csv
from datetime import datetime
from operator import attrgetter


class Customer(object):
    def __init__(self, table):
        self.id = table['id']
        self.name = table['name']
        self.gender = table['gender']
        self.birthday = datetime.strptime(table['birthday'], '%d/%m/%Y')
        self.email = table['email']
        self.active = True if table['active'] == 'True' else False

    def __str__(self):
        return str(vars(self))


def save_csv(file, header, content):
    with open(file, 'w', newline='') as f:
        writer = csv.DictWriter(f, delimiter=';', fieldnames=header)
        writer.writeheader()
        writer.writerows(list(map(vars, content)))


def save_txt(file, content):
    with open(file, 'w') as f:
        for line in content:
            f.write(str(line) + '\n')


with open('/temp/customers.csv', 'r', encoding='utf-8') as f:
    # read customers into list if Customers
    reader = csv.DictReader(f, delimiter=';')
    customers = [Customer(c) for c in reader]

    # filter active customers sorted by id
    sorted_active_customers = sorted(list(filter(lambda c: c.active, customers)), key=attrgetter('id'))

    # filter inactive male customers sorted by name
    inactive_male_customers = list(filter(lambda c: c.active == False and c.gender == 'Male', customers))
    sorted_inactive_male_customers = sorted(inactive_male_customers, key=attrgetter('name'))

    # save CVS file
    header = ['id', 'name', 'gender', 'birthday', 'email', 'active']
    save_csv('/temp/actives.csv', header, sorted_active_customers)

    # save TXT file
    save_txt('/temp/male_inactives.txt', sorted_inactive_male_customers)
