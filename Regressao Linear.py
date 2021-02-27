import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.DataFrame({'mes':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],'faturamento':[25, 38, 29, 115, 82, 114, 120, 160, 153, 190, 239, 175]})
x = df['mes']
y = df['faturamento']

tam = len(df)
somaxy = (x*y).sum()
xy = x.sum() * y.sum()
somax2 = (x**2).sum()
soma2x = x.sum()*x.sum()

m = ((tam *somaxy) - xy) / ((tam * somax2) - soma2x)
b = ( y.sum() - m*x.sum() ) / tam
xpred = 4  # previsao do quarto mes, variavel influenciadora independente
ypred = m*xpred + b #variavel afetada, dependente

predicoes = [] # lista vazia para preencher com a quantidade de valores constantes no vetor x, meses

for elemento in x:
 ypred = m*elemento + b
 predicoes.append(ypred.round(2))

df['Predicoes'] = predicoes
df['Diferenca'] = predicoes-y
df['Variacao(%)'] = (df['Predicoes']/df['faturamento']-1).round(2)*100
df['Status'] = ['Lucro' if var >0 else 'Prejuizo' for var in df['Diferenca']]
print (df)