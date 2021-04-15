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

#gerando y a partir dos coeficientes calculados

vetory1=np.empty((100)) #array para receber vetor com ruido
cont2=0
while cont2<100: 
    vetory1[cont2]=-0.5+0.4*vetorx[cont2]
    cont2=cont2+1
    
print(vetory1,' é a solucao para a equacao dada') 


#adicionando criando ruido gaussiano

aleat=np.random.randn(100) #apoio para criar ruido gaussiano
ruido=np.empty(100) #define tamanho do vetor de ruido
for i in range (0,100): #cria o vetor de ruido multiplicando por 0.1
    ruido[i]=(aleat[i]*0.1)

vetory2=np.empty((100)) #array para receber vetor com ruido

#aplicando ruido no vetor anterior
cont3=0
while cont3<100: 
    vetory2[cont3]=vetory1[cont3]+aleat[cont3]
    cont3=cont3+1

print(vetory2, ' adicao dos ruidos')

print(regressaolinear(vetorx,vetory1),'equacao da questao')
print(regressaolinear(vetorx,vetory2),'distribuicao nova pos ruido')
""" a adicao do ruido em cada indice do novo vetor y alterou a dispersao dos pontos
fazendo com que os coeficientes mudem de valor"""

import matplotlib as mp


