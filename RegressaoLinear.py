# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 22:50:48 2021

@author: Camila
"""

import numpy as np


#criando a funcao de regressão linear
def regressaolinear(x,y):
    matriz=np.empty((len(x),2)) #matriz que recebe x na 1a coluna
    i=0 #contador para percorrer todo vetor x
    while i<len(x):
        matriz[i,0]=x[i]
        matriz[i,1]=1
        i=i+1
    #calculo da transposta
    mattransp=matriz.T
    #calculo da inversa da multiplicacao de uma transposta pela matriz
    primargumento=np.linalg.inv(np.dot(mattransp,matriz))
    #calculo 2o elemento da formula que recebe y
    segunargumento=np.dot(mattransp,y)
    #calculo dos fatores
    resultado=np.dot(primargumento,segunargumento)
    return resultado
    
#chamada da funcao com 2 vetores
fatoresAeB=(regressaolinear([50,60,100,120],[30,35,41,50]))
print(fatoresAeB)

#desmembra coeficientes da reta obtidos na funcao
a=fatoresAeB[0]
b=fatoresAeB[1]

#testando vetor de 100 elementos para criar vetor y
vetorx=np.random.randn(100) #cria vetor x

#gerando y a partir dos coeficientes calculados

vetory=np.empty((100)) #criando array para receber o resultado

cont=0
while cont<100: 
    vetory[cont]=a*vetorx[cont]+b 
    cont=cont+1

print(vetory,' é a solução para o vetor aplicado nos coeficientes calculados pela função')

