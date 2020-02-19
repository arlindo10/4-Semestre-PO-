import numpy as np
from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys

def partitionForQuickSort(newList,startIndex,endIndex): 
    i = ( startIndex-1 )         
    pivot = randint(startIndex, endIndex) 
  
    for j in range(startIndex , endIndex): 
  
        if   newList[j] <= pivot: 
          
            i = i+1 
            newList[i],newList[j] = newList[j],newList[i] 
  
    newList[i+1],newList[endIndex] = newList[endIndex],newList[i+1] 
    return ( i+1 ) 

def quickSort(newList,startIndex,endIndex): 
  
    if startIndex < endIndex: 
  
        pivot = partitionForQuickSort(newList,startIndex,endIndex) 

        quickSort(newList, startIndex, pivot-1) 
        quickSort(newList, pivot+1, endIndex) 


def listInv(tamanho):
  lista =[]
  for i in range(tamanho, 0, -1):
    lista.append(tamanho)
    tamanho = tamanho - 1
  return lista


def desenhaGrafico(x, yInv,XAxis = "Lista de Numeros", YAxis = "Tempo de ordenação"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,yInv, label = "Caso(Invertida)")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(YAxis)
    plt.xlabel(XAxis)
    fig.savefig(YAxis)
    plt.show()

def startingQuickSort(newList):
  quickSort(newList, 0, len(newList) -1)

sys.setrecursionlimit(10**6)    
value100k = 100000
value200k = 200000
value300k = 300000
value400k = 400000
value500k = 500000


listInvertedCase100k = listInv(value100k)
listInvertedCase200k = listInv(value200k)
listInvertedCase300k = listInv(value300k)
listInvertedCase400k = listInv(value400k)
listInvertedCase500k = listInv(value500k)


listValue1 = [100 ,200 ,300, 400, 500]
listQuestionInvertedCase = [listInvertedCase100k,listInvertedCase200k,listInvertedCase300k,listInvertedCase400k,listInvertedCase500k]
timeSortInvertedCase = []

for i in range(5):
    timeSortInvertedCase.append(timeit.timeit("startingQuickSort({})".format(listQuestionInvertedCase[i]),setup="from __main__ import startingQuickSort, quickSort,partitionForQuickSort, listInv",number = 1))
   # print(i)

    
desenhaGrafico(listValue1,timeSortInvertedCase, XAxis="Número de elementos em milhares", YAxis="Tempo de ordenação em Seg")
