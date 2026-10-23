import csv


def process_file(filename):
    # open input file for reading
    input_file = open(filename, 'r')

    # create lists
    males = []
    females = []
    without_gender = []
    heroes_studios = []
    heroes_bad = ['']

    # csv reader without header
    reader = csv.reader(input_file)
    next(reader)

    # iterate over file lines
    for hero in reader:
        csv_content = [hero[0].strip(), hero[1].strip()]

        if hero[2].strip().lower() == 'male':
            males.append(csv_content)
        elif hero[2].strip().lower() == 'female':
            females.append(csv_content)
        else:
            without_gender.append(csv_content)

        if(hero[7].strip().lower() == 'dc comics' or
            hero[7].strip().lower() == 'marvel comics'):
            heroes_studios.append(hero[1])

        if(hero[8].strip().lower() == 'blue' and
            hero[9].strip().lower() == 'bad'):
            heroes_bad[0] = heroes_bad[0] + hero[1] + '#'

    header = ['id', 'name']
    save_csv('F:/Documentos/Python_Projects//heroes_male.csv', header, males)
    save_csv('F:/Documentos/Python_Projects//heroes_female.csv', header, females)
    save_csv('F:/Documentos/Python_Projects//heroes_without_gender.csv', header, without_gender)
    save_txt('F:/Documentos/Python_Projects//heroes_studio.txt', heroes_studios)
    save_txt('F:/Documentos/Python_Projects//heroes_bad.txt', heroes_bad)
    input_file.close()

def save_csv(file, header, content):
    f = open(file, 'w', newline='')
    writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(header)
    writer.writerows(content)
    f.close()

def save_txt(file, content):
    f = open(file, 'w')
    for line in content:
        f.write(line + '\n')
    f.close()

process_file('F:/Documentos/Python_Projects/heroes_information.csv')