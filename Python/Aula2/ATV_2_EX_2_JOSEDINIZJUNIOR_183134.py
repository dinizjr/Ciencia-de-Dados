import csv

def showinformation(file):

    total_acidentes = 0
    tipos = []
    tipos_uniq = []
    tipo_aviao = 0
    tipo_helicoptero = 0
    tipo_ultraleve = 0
    ano_fab = []
    new_ano = []
    old_ano = []
    old_year_manufact = []
    new_seat = []
    helicoptero = 0
    aviao = 0
    new_engine = 0


    with open(file, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)

        for line in reader:
            total_acidentes += 1
            tipos.append(line[1])
            tipos_uniq = list(set(tipos))
            if line[1] == 'AVIÃO':
                tipo_aviao += 1
            if line[1] == 'HELICÓPTERO':
                tipo_helicoptero += 1
            if line[1] == 'ULTRALEVE':
                tipo_ultraleve += 1
            ano_fab.append(line[5])
            new_ano = max(ano_fab)
            old_ano = min(ano_fab)
            if line[5] == old_ano:
                old_year_manufact = (line[2])
            if line[5] == new_ano:
                new_seat = (line[6])
                new_engine = (line[3])
            if line[1] == 'HELICÓPTERO' and line[5] > '1997':
                helicoptero += int(line[7])
            if line[1] == 'AVIÃO' and line[2] == 'CESSNA AIRCRAFT':
                aviao += 1

        print('Quantidade total de acidentes: ' + str(total_acidentes).strip('.0'))
        print('Quantidade total de acidentes agrupados por tipo: ' "Avião: " + str(tipo_aviao) + ', ' +  "Helicóptero: " + str(tipo_helicoptero) + ', ' + "Ultraleve: " + str(tipo_ultraleve))
        print('Ano e fabricante da aeronave mais antiga: ' 'Ano: '+ old_ano + ', ' + 'Fabricante:  '+ (old_year_manufact))
        print('Quantidade de assentos e tipo de motor da aeronave mais nova: Assentos: ' + str(new_seat) + ', Tipo motor: ' + new_engine)
        print('Quantidade de acidentes de helicópteros fabricado após 1997: ' + str(helicoptero))
        print('Quantidade de acidentes de avião fabricado pela Cessna Aircraft: ' + str(aviao))

showinformation('C:/Software Splice/Python/levels.csv')