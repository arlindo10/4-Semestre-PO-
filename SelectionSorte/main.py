import numpy as np
from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt


def SelectionSort(elementList):
  swappedNumber = 0
  for i in range(len(elementList)): 
      
    minIndex = i 
    for j in range(i+1, len(elementList)): 
      swappedNumber = swappedNumber + 1
      if elementList[minIndex] > elementList[j]: 
        minIndex = j
            
    if minIndex != 1:
      elementList[i], elementList[minIndex] = elementList[minIndex], elementList[i]
  return swappedNumber


def listInv(tamanho):
  lista =[]
  for i in range(tamanho, 0, -1):
    lista.append(tamanho)
    tamanho = tamanho - 1
  return lista


def desenhaGrafico(x,y,yInv,XAxis = "Lista de Numeros", YAxis = "Tempo de ordenação"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Aleatorio")
    ax.plot(x,yInv, label = "Pior Caso(Invertida)")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(YAxis)
    plt.xlabel(XAxis)
    fig.savefig(YAxis)
    plt.show()

def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista    

value1k = 100
value10k = 10000
value30k = 60000
value60k = 100000

list1k = geraLista(value1k)
list10k = geraLista(value10k)
list30k = geraLista(value30k)
list60k = geraLista(value60k)

listWorseCase1k = listInv(value1k)
listWorseCase10k = listInv(value10k)
listWorseCase30k = listInv(value30k)
listWorseCase60k = listInv(value60k)

listValue = [value1k,value10k,value30k,value60k]
listQuestion = [list1k,list10k,list30k,list60k]
listQuestionWorseCase = [listWorseCase1k, listWorseCase10k, listWorseCase30k, listWorseCase60k]
timeSort = []
timeSortWorseCase = []
listNumberSwap = []
listNumberSwapWorseCase = []

for i in range(4):
    timeSort.append(timeit.timeit("SelectionSort({})".format(listQuestion[i]),setup="from __main__ import geraLista,SelectionSort, listInv",number = 1))
    listNumberSwap.append(SelectionSort(listQuestion[i]))
    timeSortWorseCase.append(timeit.timeit("SelectionSort({})".format(listQuestionWorseCase[i]),setup="from __main__ import geraLista,SelectionSort, listInv",number = 1))
    listNumberSwapWorseCase.append(SelectionSort(listQuestionWorseCase[i]))

desenhaGrafico(listValue,timeSort,timeSortWorseCase, XAxis="Número de elementos", YAxis="Tempo de ordenação em Seg")
desenhaGrafico(listValue,listNumberSwap,listNumberSwapWorseCase,  XAxis="Número de elementos", YAxis="Numero de Trocas")
