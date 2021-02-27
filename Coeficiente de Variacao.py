import numpy as np
import pandas as pd


def calcula(vet):
  resultado = np.std(vet, ddof=1) / np.mean(vet) * 100 
  return resultado

data = pd.read_csv('weight-height.csv')
data['Altura'] = data['Height']*2.54
data['Altura'] = data['Altura'].round(0)
data['Peso'] = data['Weight']*0.453592
data['Peso'] = data['Peso'].round(1)

male = data.loc[data['Gender']=='male']	
female = data.loc[data['Gender']=='female']
df = pd.DataFrame()
print()

#Calculo Mulheres
salt = pd.Series(female['Altura'].values)
speso = pd.Series(female['Peso'].values)

df['Genero'] = ['Mulher']
df['Media Altura'] = salt.mean().round(0)
df['Mediana Altura'] = salt.median().round(0)
df['Moda Altura'] = salt.mode().round(0)
df['Coeficiente Altura'] = calcula(female['Altura']).round(0)
df['Media Peso'] = speso.mean().round(1)
df['Mediana Peso'] = speso.median().round(1)
df['Moda Peso'] = speso.mode().round(1)
df['Coeficiente Peso'] = calcula(female['Peso']).round(1)	
print (df)
print()

#Calculo Homens
salt = pd.Series(male['Altura'].values)
speso = pd.Series(male['Peso'].values)

df['Genero'] = ['Homen']
df['Media Altura'] = salt.mean().round(0)
df['Mediana Altura'] = salt.median().round(0)
df['Moda Altura'] = salt.mode().round(0)
df['Coeficiente Altura'] = calcula(male['Altura']).round(0)	
df['Media Peso'] = speso.mean().round(1)
df['Mediana Peso'] = speso.median().round(1)
df['Moda Peso'] = speso.mode().round(1)
df['Coeficiente Peso'] = calcula(male['Peso']).round(1)	

print (df)