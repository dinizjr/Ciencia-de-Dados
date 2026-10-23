import pandas as pd
import numpy as np


eqp = pd.read_csv(r'F:\Arquivos\Ciência de Dados\Python_Prog_DS\titanic_data.csv', delimiter=';')
print(eqp.head(20))
#arr = np.array(eqp.loc[:,2])
#eqp['mês'] = [f.split(sep='/')[1] for f in arr]
#print(data.head())

