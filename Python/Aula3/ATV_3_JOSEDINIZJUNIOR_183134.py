import csv
import operator
import json
import itertools
import statistics
import threading

#criação da classe Election2016
class Election2016(object):
    def __init__(self, data):
        self.cod_municipio_tse  = data['cod_municipio_tse']
        self.uf                 = data['uf']
        self.nome_municipio     = data['nome_municipio']
        self.total_eleitores    = data['total_eleitores']
        self.f_16               = data['f_16']
        self.f_17               = data['f_17']
        self.f_18_20            = data['f_18_20']
        self.f_21_24            = data['f_21_24']
        self.f_25_34            = data['f_25_34']
        self.f_35_44            = data['f_35_44']
        self.f_45_59            = data['f_45_59']
        self.f_60_69            = data['f_60_69']
        self.f_70_79            = data['f_70_79']
        self.f_sup_79           = data['f_sup_79']
        self.gen_feminino       = data['gen_feminino']
        self.gen_masculino      = data['gen_masculino']
        self.gen_nao_informado  = data['gen_nao_informado']

#criação da clasee Thread
class Save_in_Thread(threading.Thread):
    def __init__(self, output, file, header):
        threading.Thread.__init__(self)
        self.output = output
        self.file = file
        self.header = header

    def run(self):
        with open(file=self.output, mode='w', encoding='utf8', newline='') as writecsv:
            writer = csv.DictWriter(writecsv,delimiter=';',fieldnames=self.header)
            writer.writeheader()
            writer.writerows(list(map(vars,self.file)))

#Abrir e salvar arquivo csv classificado por uf e cod_municipio
def savecsv(file, header, content):
    with open(file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=header)
        writer.writeheader()
        writer.writerows(list(map(vars,content)))

def loadfile(file):
    with open(file, 'r', encoding='utf-8') as opencsv:
        reader = csv.DictReader(opencsv, delimiter=';')
        headercontent = reader.fieldnames
        Election_2016 = [Election2016(e) for e in reader]
        return Election_2016, headercontent


#Listar tuplas com quantidade de eleitoras por estado
def group_female_by_uf(file):
    list_female = []

    female_group = list(map(lambda x: {'uf':x.uf, 'fem':x.gen_feminino}, file))

    for key, group in itertools.groupby(female_group, key=lambda x: x['uf']):
        list_female.append((key, sum(list(map(lambda x: int(x['fem']), group)))))
    return list_female

#Salvar arquivo json com estatísticas baseado na lista de eleitoras por estado
def pleito_2016_stat_json(file, output):
    list_fem = list(map(lambda x: x[1], file))

    data_json = {
        'média': statistics.mean(list_fem),
        'mediana': statistics.median(list_fem),
        'variância': statistics.variance(list_fem),
        'desvio_padrão': statistics.stdev(list_fem)
    }

    with open(file=output, mode='w', encoding='utf-8') as savejason:
            json.dump(obj=data_json, fp=savejason, ensure_ascii=False, indent=2)

#chamar Thread a gravar csv por estado
def save_election_by_uf(file, header):
    data_grouped = itertools.groupby(file, key=lambda x: x.uf)
    for key, group in data_grouped:
        Save_in_Thread('F:/Documentos/Python_Projects/saida_atv3/' + key + '.csv', list(group), header).start()


election_2016, header = loadfile('F:/Documentos/Python_Projects/BR_eleitorado_2016_municipio.csv')
sorted_uf_mun = sorted(election_2016, key=operator.attrgetter('uf', 'cod_municipio_tse'))
savecsv('F:/Documentos/Python_Projects/saida_atv3/pleito_2016_classificado.csv', header, sorted_uf_mun)
print('Arquivo pleito_2016_classificado.csv carregado com sucesso')
List_female = group_female_by_uf(sorted_uf_mun)
print('Lista com informações de eleitoras por estado: ' + str(List_female)) #listar tuplas
print('Arquivo pleito_2016_stat.json carregado com sucesso')
pleito_2016_stat_json(List_female, 'F:/Documentos/Python_Projects/saida_atv3/pleito_2016_stat.json')
save_election_by_uf(sorted_uf_mun, header)
print('Arquivos csv por estado gravados com sucesso ')

