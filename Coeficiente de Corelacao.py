import numpy as np
import pandas as pd
import math

df = pd.DataFrame({'mes':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],'faturamento':[25, 38, 29, 115, 82, 114, 120, 160, 153, 190, 239, 175]})
x = df['mes']
y = df['faturamento']

tam = len(df)
somaxy = (x*y).sum()
xy = x.sum() * y.sum()
somax2 = (x**2).sum()
soma2x = x.sum()*x.sum()
somay2 = (y**2).sum()
soma2y = y.sum()*y.sum()

r = (tam*somaxy - xy)/(math.sqrt( (tam*somax2 - soma2x)*(tam*somay2 - soma2y))) #Representa a qualidade dos dados/correlaçao ( reflexo com a realidade ), quanto mais proximo de 1 melhor
b1 = (tam*somaxy - xy) / (tam*somax2 - soma2x) # Inclinação da reta
b0 = (y.sum() - (b1*x.sum()))/tam # Interceptação da reta no eixo Y

rel = None
if r>0.9 and r<=1.0:
 rel='Otima'
elif r>0.8 and r<=0.9:
 rel='Boa'
elif r>0.7 and r<=0.8:
 rel='Razoavel'
elif r>0.6 and r<=0.7:
 rel='Mediocre'
elif r>0.5 and r<=0.6:
 rel='Pessima'
elif  r<=0.5:
 rel='Impropria'

df ['Regressao Linear'] = (b0+(b1*x)).round(2)
print()
print('Resultados: B1= '+str(b1.round(2))+', B0= '+str(b0.round(2)))
print ('Dados com qualidade '+rel+': '+str(r.round(4)))
print()
print(df.to_string(index=False))