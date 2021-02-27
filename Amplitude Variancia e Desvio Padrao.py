import numpy
import pandas as pd

A = pd.Series([5,5,5,5,5])
B = pd.Series([3,4,5,6,7])
C = pd.Series([13,14,15,16,17])
D = pd.Series([1,3,5,7,9])
E = pd.Series([3,5,5,5,7])
F = pd.Series([3,3,4,4,5,5,6,6,6,7,7])

def mostra(letra):
 print(letra+' => AMPLITUDE: '+str(amplitude))
 print(letra+' => DESVIO: '+str(desvioPadrao))
 print (letra+' => VARIANCIA: '+str(variancia))
 print()

vetores = ['A','B','C','D','E','F']
for vet in vetores:
 variancia = eval(vet+'.var(ddof=1)')
 desvioPadrao = eval(vet+'.std(ddof=1)')
 amplitude = int(eval(vet+'.max()')) - int(eval(vet+'.min()'))
 mostra(let)