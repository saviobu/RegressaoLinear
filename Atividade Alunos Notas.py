import numpy
import pandas as pd

notas = pd.Series([9,9,8,8,4,4,6,6,6,7,10])

print ('MEDIA: '+str(notas.mean()))
print ('MEDIANA: '+str(notas.median()))
print ('MODA: '+str(notas.mode()))
print ('VARIANCIA: '+str(notas.var(ddof=1)))
print ('DESVIO: '+str(notas.std(ddof=1)))
print ('AMPLITUDE: '+str(max(notas)-min(notas)))