
import numpy as np
from random import randint, shuffle
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys


def startingMergeSort(elementList):
	mergeSort(elementList, 0, len(elementList)-1)
	
def mergeSort(elementList, first, last):
	if first < last:
		middle = (first + last)//2
		mergeSort(elementList, first, middle)
		mergeSort(elementList, middle+1, last)
		merging(elementList, first, middle, last)
		
def merging(elementList, first, middle, last):
	L = elementList[first:middle+1]
	R = elementList[middle+1:last+1]
	L.append(sys.maxsize)
	R.append(sys.maxsize)
	i = j = 0
	
	for k in range (first, last+1):
		if L[i] <= R[j]:
			elementList[k] = L[i]
			i += 1
		else:
			elementList[k] = R[j]
			j += 1


def drawGraph(x,y,yInv,XAxis = "Lista de Numeros", YAxis = "Tempo de ordenação"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y,color = 'blue', label = "Aleatorio")
    ax.plot(x,yInv, color = 'red', label = "Invertida")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(YAxis)
    plt.xlabel(XAxis)
    fig.savefig(YAxis)
    plt.show()


def listInv(tamanho):
  newList =[]
  for i in range(tamanho, 0, -1):
    newList.append(tamanho)
    tamanho = tamanho - 1
  return newList


def generateList(tam):
  newList = list(range(1, tam + 1))
  shuffle(newList)
  return newList

sys.setrecursionlimit(10**6)  

listValueGraph = [2000 ,4000 , 6000, 8000, 100000]
#~~~~~~~~~~ Tests ~~~~~~~~~~~#


value20k = 20000
value40k = 40000
value60k = 60000
value80k = 80000
value100K = 1000000


#~~~~~~~~~~ List Inverted Case ~~~~~~~~~~~#

listInvertedCase20k = generateList(value20k)
listInvertedCase40k = listInv(value40k)
listInvertedCase60k = listInv(value60k)
listInvertedCase80k = listInv(value80k)
listInvertedCase100K = listInv(value100K)



listQuestionInvertedCase = [listInvertedCase20k,listInvertedCase40k,
                            listInvertedCase60k,listInvertedCase80k, 
                            listInvertedCase100K]
timeSortInvertedCase = []

#~~~~~~~~~~ Random List Case ~~~~~~~~~~~#

listRandomCase20k = generateList(value20k)
listRandomCase40k = generateList(value40k)
listRandomCase60k = generateList(value60k)
listRandomCase80k = generateList(value80k)
listRandomCase100K = generateList(value100K)



listQuestionRandomCase = [listRandomCase20k,listRandomCase40k,
                          listRandomCase60k, listRandomCase80k, 
                          listRandomCase100K]
timeSortRandomCase = []
for i in range(5):
    timeSortInvertedCase.append(timeit.
                                timeit("startingMergeSort({})".format(listQuestionInvertedCase[i]),
                                              setup="from __main__ import startingMergeSort,mergeSort,merging, listInv, generateList",number = 1))
    timeSortRandomCase.append(timeit.
                              timeit("startingMergeSort({})".format(listQuestionRandomCase[i]),
                                            setup="from __main__ import startingMergeSort,mergeSort,merging, listInv, generateList",number = 1))
    print(i)

#

drawGraph(listValueGraph,
          timeSortInvertedCase,
          timeSortRandomCase, 
          XAxis="Número de elementos em milhares", 
          YAxis="Tempo de ordenação em Seg")
