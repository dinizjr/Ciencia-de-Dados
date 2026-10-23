import pandas as pd
import numpy as np

desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows', None)

df = pd.read_excel(open('C:/Software Splice/Planilhas/cartao_caminhao_Exportada_em_10-12-2018.xls','rb'), sheet_name='planilha_0')
#print(df.VEÍCULO)
#df = pd.DataFrame(df)
#validade = []

#print(df)

for row in df:
    i = 1
    validade = df.VALIDADE.str.replace('/', '')
    placa = df.VEÍCULO.str.replace('-', '')
    data = pd.Series([validade[i]],[placa[i]])
    i += 1
    print(data)