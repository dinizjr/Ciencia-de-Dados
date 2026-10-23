# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import pandas as pd

df = pd.read_csv('C:\Software Splice\Python\levels.csv')
print(df)

df['seating'].plot('bar')