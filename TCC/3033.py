import pandas as pd
import numpy as np


eqp = pd.read_csv('C:/Software Splice/Planilhas/3033.csv', delimiter=';')
print(eqp.head())

arr = np.array(eqp.loc[:,2])
eqp['mês'] = [f.split(sep='/')[1] for f in arr]
print(data.head())