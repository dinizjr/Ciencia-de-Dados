import csv
import pandas as pd
#import plotly.graph_objs as go
#from plotly.offline import init_notebook_mode, iplot
#init_notebook_mode(connected=True)
import numpy as np

#import matplotlib.pyplot as plt
import matplotlib
#%matplotlib inline
matplotlib.rcParams['font.size'] = 12
matplotlib.rcParams['figure.dpi'] = 150

'''import seaborn as sns
from IPython.core.pylabtools import figsize
from matplotlib.ticker import FormatStrFormatter'''

dfMT = pd.read_csv('C:/Software Splice/Python/Meteorologia.csv',delimiter=',',encoding='utf-8')
#dfMT.info()

dfMT['hora'] = pd.to_datetime(dfMT['data']).dt.hour
dfMT['dia'] = pd.to_datetime(dfMT['data']).dt.day

temp = pd.DataFrame(dfMT.groupby('dia').temperatura_ar_vmedio.mean()).reset_index()

print(temp.plot())

