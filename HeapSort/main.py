
import numpy as np
from random import shuffle, randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
import math

mpl.use('Agg')
mpl.rc('lines', linewidth=2.9)
plt.style.use('ggplot')

sys.setrecursionlimit(10**7) 






def heapSort(a):  
  
    def swap(a,i,j):  
        tmp = a[i]  
        a[i] = a[j]  
        a[j] = tmp    
          
    def siftdown(a, i, size):  
        l = 2*i+1  
        r = 2*i+2  
        largest = i  
        if l <= size-1 and a[l] > a[i]:  
            largest = l  
        if r <= size-1 and a[r] > a[largest]:  
            largest = r  
        if largest != i:  
            swap(a, i, largest)  
            siftdown(a, largest, size)  
              
    def heapify(a, size):  
        p = (size//2)-1  
        while p>=0:  
            siftdown(a, p, size)  
            p -= 1  
              
    size = len(a)          
    heapify(a, size)  
    end = size-1  
    while(end > 0):  
        swap(a, 0, end)  
        siftdown(a, 0, end)  
        end -= 1
        
        
        
def drawGraph(x,y,yInv,XAxis = "Lista de Numeros", YAxis = "Tempo de ordenação", name =" Tempo de ordenação em seg"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    plt.scatter(x,y,marker='^',facecolor='red',edgecolors= 'red', linewidths=4)  
    ax.plot(x,y,color = 'blue', markerfacecoloralt ='green', label = "Aleatorio")
    plt.scatter(x,yInv,marker= 'v',facecolor='blue',edgecolors= 'blue', linewidths=4)  
    ax.plot(x,yInv, color = 'red', label = "Invertida")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(YAxis)
    plt.xlabel(XAxis)
    fig.savefig(name)
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


listValueGraph =  [15000,25000,35000,45000,55000]
#~~~~~~~~~~ Tests ~~~~~~~~~~~#


value15k = 15000
value25k = 25000
value35k = 35000
value45k = 45000
value55k = 55000

#~~~~~~~~~~ List Inverted Case ~~~~~~~~~~~#

listInvertedCase15k = listInv(value15k)
listInvertedCase25k = listInv(value25k)
listInvertedCase35k = listInv(value35k)
listInvertedCase45k = listInv(value45k)
listInvertedCase55k = listInv(value55k)



listQuestionInvertedCase = [listInvertedCase15k,listInvertedCase25k,
                            listInvertedCase35k,listInvertedCase45k,
                            listInvertedCase55k]

timeSortInvertedCase = []



#~~~~~~~~~~ Random List Case ~~~~~~~~~~~#

listRandomCase15k = generateList(value15k)
listRandomCase25k = generateList(value25k)
listRandomCase35k = generateList(value35k)
listRandomCase45k = generateList(value45k)
listRandomCase55k = generateList(value55k)




listQuestionRandomCase = [listRandomCase15k,listRandomCase25k,
                          listRandomCase35k,listRandomCase45k,
                          listRandomCase55k] 
timeSortRandomCase = []




for i in range(5):
    timeSortInvertedCase.append(timeit.
                                timeit("heapSort({})".format(listQuestionInvertedCase[i]),
                                              setup="from __main__ import heapSort, listInv, generateList",number = 1))
    timeSortRandomCase.append(timeit.
                              timeit("heapSort({})".format(listQuestionRandomCase[i]),
                                            setup="from __main__ import heapSort, listInv, generateList",number = 1))
    
    print(i)


drawGraph(listValueGraph,
          timeSortInvertedCase,
          timeSortRandomCase, 
          XAxis="Número de elementos em milhares", 
          YAxis="Tempo de ordenação em Seg",
         name = "Tempo de ordenação em Seg HeapSort")
