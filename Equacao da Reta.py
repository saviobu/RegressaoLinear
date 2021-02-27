#Exercicios

import numpy as np
import pandas as pd


#Exercicio 1

def calcula1(vet):
 return (vet['B'][1]-vet['A'][1])/(vet['B'][0]-vet['A'][0])
  
A = pd.DataFrame({'A':[3,2],'B':[-3,-1]})
B = pd.DataFrame({'A':[2,-3],'B':[-4,3]})
C = pd.DataFrame({'A':[3,2],'B':[3,-2]})
D = pd.DataFrame({'A':[-1,4],'B':[3,2]})	
E = pd.DataFrame({'A':[5,2],'B':[-2,-3]})
F = pd.DataFrame({'A':[200,100],'B':[300,80]})

vetores1 = ['A','B','C','D','E','F'] 
print()
print ('** Exercicio 1 **')
print()
for vetor in vetores1:
 print (vetor+' => ' +str(calcula1(eval(vetor))))

#Exercicio 2

def calcula2(vet,m):
 t1 = round(m,1)
 t2 = (m*vet['A'][0]).round(1)-vet['A'][1]
 
 if t1>0:
  t1 = '-'+str(t1)
 else:
  t1 = '+'+str(t1)[1:]
  
 if t2>0:
  t2 = '+'+str(t2)
 else:
  t2 = str(t2)

 return 'Y'+t1+'X'+t2+' = 0' # y-mx+mx1-y1 = 0
	
A = pd.DataFrame({'A':[-1,-2],'B':[5,2]})
B = pd.DataFrame({'A':[-1,6],'B':[2,-3]})
C = pd.DataFrame({'A':[-1,8],'B':[-5,-1]})
D = pd.DataFrame({'A':[5,0],'B':[-1,-4]})	
E = pd.DataFrame({'A':[3,3],'B':[1,-5]})

vetores2 = ['A','B','C','D','E'] 

print()
print ('** Exercicio 2 **')
print()
for vetor in vetores2:
 m = calcula1(eval(vetor)) 
 print(vetor+' => '+calcula2(eval(vetor),m))

#Exercicio 3

def calcula3(mat):
 return np.linalg.det(mat)

A = [[8,5,1],[-2,3,1],[4,1,1]]	
B = [[6,5,1],[-2,3,1],[4,1,1]]	
C = [[-5,5,1],[-2,3,1],[4,1,1]]	
D = [[-8,5,1],[-2,3,1],[4,1,1]]	
E = [[7,5,1],[-2,3,1],[4,1,1]]	

vetores3 = ['A','B','C','D','E'] 

print()
print ('** Exercicio 3 **')
print()

for vet in vetores3:
 if calcula3(eval(vet)) == 0:
  print('Resposta Exercicio 3 letra : '+vet+') '+str(eval(vet)[0][0]))


#Exercicio 4

A = 'Y+1.0X-1.0 = 0'
B = 'Y+1.0X+1.0 = 0'
C = 'Y+1.0X-3.0 = 0'
D = 'Y+1.0X+3.0 = 0'
E = '-Y+1.0X+3.0 = 0'

vetores4 = ['A','B','C','D','E'] 

val = pd.DataFrame({'A':[-1,-2]})
m = -1.0
eq = calcula2(val,m)

print()
print('** Exercicio 4 **')
print()

for vet in vetores4:
 if (eval(vet)==eq):
  print('Resposta Exercicio 4 : '+vet+') '+eq)


#Exercicio 5 ( **premissa dividir a equaçao pelo valor de y, com uma casa e colocar Y positivo sempre)

A = 'Y-0.7X+4.3 = 0' #'-3.0Y+2.0X-13.0 = 0'
B = 'Y+0.7X-4.3 = 0' #'-3.0Y-2.0X+13.0 = 0'
C = 'Y-1.5X-7.5 = 0' #'-2.0Y+3.0X+13.0 = 0'
D = 'Y+2.0X-4.3 = 0' #'-3.0Y+2.0X+13.0 = 0'
E = 'Y+0.7X-4.3 = 0' #'3.0Y+2.0X-13.0 = 0'

vetores5 = ['A','B','C','D','E'] 

df = pd.DataFrame({'A':[2,-3],'B':[8,1]})

m = calcula1(df)
eq = calcula2(df,m)

print()
print('** Exercicio 5 **')
print()

for vet in vetores5:
 if (eval(vet)==eq):
  print ('Resposta Exercicio 5 : '+vet+') '+eq)