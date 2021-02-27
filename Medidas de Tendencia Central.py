import numpy
import pandas as pd

val = pd.Series([2,4,6,3,2,1,4,3,5,2,1,1,4,0,2,2,5,2,2,1])

print ('Total de Itens : '+str(val.count()))
print ('Total por Itens :')
print (val.value_counts())
print ('Media : '+str(val.mean()))
print ('Mediana :'+str(val.median()))
print ('Moda : '+str(val.mode()[0]))