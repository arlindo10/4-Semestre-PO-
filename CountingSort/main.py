import numpy as np
from random import shuffle, randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt


mpl.use('Agg')
mpl.rc('lines', linewidth=2.9)
plt.style.use('ggplot')


def countingSort(lista):   #Complexidade Temporal = O(n+k), n para numero de elementos e k o tamanho da lista
  k = max(lista)
  B = [0 for w in range(len(lista))]
  C = [0 for w in range(k+1)]
  for j in range(0,len(lista)):
    C[lista[j]] = C[lista[j]] + 1
  for i in range(1,k+1):
    C[i] += C[i-1]
  for j in range(len(lista)-1,0,-1):
    B[C[lista[j]]-1] = lista[j]
    C[lista[j]] = C[lista[j]] - 1
  return B

def listInv(tamanho):
  lista =[]
  for i in range(tamanho, 0, -1):
    lista.append(tamanho)
    tamanho = tamanho - 1
  return lista


def drawGraph(x,y,yInv,XAxis = "Lista de Numeros", YAxis = "Tempo de ordenação"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    plt.scatter(x,y,marker='^',facecolor='red',edgecolors= 'red', linewidths=4)  
    ax.plot(x,y,color = 'blue', markerfacecoloralt ='green', label = "Aleatorio")
    plt.scatter(x,yInv,marker= 'v',facecolor='blue',edgecolors= 'blue', linewidths=4)  
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

 

listValueGraph = [30000, 40000, 50000, 60000, 70000]
#~~~~~~~~~~ Tests ~~~~~~~~~~~#

value30k = 30000
value40k = 40000
value50k = 50000
value60k = 60000
value70k = 70000


#~~~~~~~~~~ List Inverted Case ~~~~~~~~~~~#

listInvertedCase30k = listInv(value30k)
listInvertedCase40k = listInv(value40k)
listInvertedCase50k = listInv(value50k)
listInvertedCase60k = listInv(value60k)
listInvertedCase70k = listInv(value70k)

listQuestionInvertedCase = [listInvertedCase30k,listInvertedCase40k,
                            listInvertedCase50k,listInvertedCase60k, 
                            listInvertedCase70k]
timeSortInvertedCase = []

#~~~~~~~~~~ Random List Case ~~~~~~~~~~~#

listRandomCase30k = generateList(value30k)
listRandomCase40k = generateList(value40k)
listRandomCase50k = generateList(value50k)
listRandomCase60k = generateList(value60k)
listRandomCase70k = generateList(value70k)



listQuestionRandomCase = [listRandomCase30k,listRandomCase40k,
                          listRandomCase50k, listRandomCase60k, 
                          listRandomCase70k] 
timeSortRandomCase = []
for i in range(5):
    timeSortInvertedCase.append(timeit.
                                timeit("countingSort({})".format(listQuestionInvertedCase[i]),
                                              setup="from __main__ import countingSort, listInv, generateList",number = 1))
    timeSortRandomCase.append(timeit.
                              timeit("countingSort({})".format(listQuestionRandomCase[i]),
                                            setup="from __main__ import countingSort, listInv, generateList",number = 1))
    print(i)

drawGraph(listValueGraph,
          timeSortInvertedCase,
          timeSortRandomCase, 
          XAxis="Número de elementos em milhares", 
          YAxis="Tempo de ordenação em Seg")
