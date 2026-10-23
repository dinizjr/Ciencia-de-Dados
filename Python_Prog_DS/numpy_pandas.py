import numpy as np
import pandas as pd
import csv

'''x = np.eye((20), dtype=int)
print(x)

arr = np.array([10,20,30])
#print(arr)
list = pd.Series(arr)
print(list)'''

#########Aterar conf para aparecer mais colunas##############
'''desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',20)
pd.set_option('display.max_rows', None)'''


tit = pd.read_csv('titanic_data.csv',delimiter=',',encoding='utf-8')
tit.head()
#x = tit.columns.tolist() #Header
#print(x)
#tit.info()

#print(tit.head(6)) first 10
#print(tit.iloc[:10]) #first 10
#print(tit.iloc[-8:]) #last 8

#print(len(tit.columns)) #numbers of columns
#print(tit['Name'].count()) #numbers of rows

'''z = tit.isnull().any() #verificar nan
x = tit.columns[z] #where is nan
y = tit[x].isnull().sum() #how many nan
print(y)'''

#a = tit['Cabin'].fillna(0) #substituir nan
#print(a)


tit.drop(tit.columns[[6,7,8]], axis=1, inplace=True) #delete columns
#print(drop_col)

header = tit.columns.tolist()
#print(header)

old = header
#print(old)
new = ['IdPassageiro', 'Sobreviveu', 'Classe', 'Nome', 'Sexo', 'Idade', 'Tarifa', 'Cabine', 'Embarque']
tit.rename(columns=dict(zip(old, new)), inplace=True) #rename columns


tit.Sobreviveu.replace({0:'Não', 1:'Sim'}, inplace=True)
tit.Sexo.replace({'female':'Mulher', 'male':'Homem'}, inplace=True)
#print(tit)

#x = tit[tit.Sexo=='Homem'].Sexo.value_counts()#.nlargest(1)
hm = tit.Sexo.value_counts()
x = tit.Sobreviveu.value_counts()
#print(x)

m_ns = tit[(tit.Sexo=='Mulher') & (tit.Sobreviveu=='Não')].Sexo.value_counts() #qts mulheres não sobreviveram

ms = tit[(tit.Sexo=='Mulher') & (tit.Sobreviveu=='Sim')].Sexo.value_counts()
hs = tit[(tit.Sexo=='Homem') & (tit.Sobreviveu=='Sim')].Sexo.value_counts()
#print(ms)

percent = pd.crosstab(tit['Sobreviveu'],tit['Sexo']).apply(lambda p: p/p.sum(), axis=1)*100
#print(percent)

sobreviventes = tit.groupby(['Sobreviveu','Sexo','Classe']).size()
#print(sobreviventes)

x = tit.groupby('Sobreviveu')['Sexo'].value_counts()
#print(type(idade))
#print(idade)

#prob = tit.groupby('Sobreviveu')['Sexo'].value_counts()/tit.groupby('Sobreviveu')['Sexo'].count()

#prob = pd.crosstab(tit['Sexo'],tit['Classe']).apply(lambda p: p/p.sum(), axis=1)
#print(prob)

'''old_names = ['$a', '$b', '$c', '$d', '$e'] 
new_names = ['a', 'b', 'c', 'd', 'e']
df.rename(columns=dict(zip(old_names, new_names)), inplace=True)'''

#df = pd.DataFrame(sobreviventes)
#print(df)

#male = df[df.Sobreviveu=='Sim'].Sexo.value_counts
#print(df)

qtd = pd.DataFrame({'qtd':tit.groupby(['Sexo','Classe','Sobreviveu']).size()}).reset_index()
#print(qtd)
female = qtd[(qtd.Sexo=='Mulher') & (qtd.Sobreviveu=='Sim')]
#print(female)
male = qtd[(qtd.Sexo=='Homem') & (qtd.Sobreviveu=='Sim')]
#print(male)
prob = male.groupby('qtd').size().div(len(male))
x = male.groupby(['Classe','qtd']).size().div(len(male)).div(prob, axis=0, level='qtd')
#print(x)

br = pd.read_csv('senado.csv',delimiter=',',encoding='ANSI')#,quotechar='"')
print(br.head())

#br.to_csv('senado_II.csv',sep=';',encoding='ANSI',quoting=csv.QUOTE_NONE,quotechar="",escapechar='\\')

br.to_csv('senado_II.csv',sep=';',encoding='ANSI')