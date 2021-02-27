import numpy
import pandas as pd

taxa = pd.Series ([56,61,57,77,62,75,63,55,64,60,60,57,61,57,67,62,69,67,68,59,65,72,65,61,68,73,65,62,75,80,66,61,69,76,72,57,75,68,83,64,69,64,66,74,65,76,65,58,65,64,65,60,65,80,66,80,68,55,66,71])

print ('TOTAL DE REGISTROS: '+str(taxa.count()))
print ('MEDIA: '+str(taxa.mean()))
print ('MEDIANA: '+str(taxa.median()))
print ('MODA: '+str(taxa.mode()[0]))
print ('VARIANCIA: '+str(taxa.var(ddof=1)))
print ('DESVIO: '+str(taxa.std(ddof=1)))
print ('AMPLITUDE: '+str(max(taxa)-min(taxa)))
print ('FREQUENCIA:')
print (taxa.value_counts())
