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

def countingSort(elementList, n, place):                                         
    integerRange = 10;                                                         
    freq =[0 for i in range(0, integerRange)];                                 
    listSorted = [0 for i in range(0, n)];                                     
                                                                                
    for i in range(0, n):                                                       
        freq[(elementList[i]//place)%integerRange] += 1;                          
                                                                                
    for i in range(1, integerRange):                                           
        freq[i] += freq[i-1];                                                   
                                                                                
    i = n-1;                                                                    
    while (i>=0):                                                               
        listSorted[freq[(elementList[i]//place)%10]-1]=elementList[i];              
        freq[(elementList[i]//place)%10] -= 1;                                     
        i -= 1;                                                                 
                                                                                
    for j in range(0, n):                                                       
        elementList[j]=listSorted[j];                                            
                                                                                
def radixSort(elementList):                                                      
    n = len(elementList);                                                         
    maxElement = max(elementList);                                               
    mul=1;                                                                      
    while (maxElement):                                                        
        countingSort(elementList, n, mul);                                       
        mul *= 10;                                                              
        maxElement /= 10;                                                      
                                                                                
    return elementList;    







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



listValueGraph = [20000 ,30000, 40000 , 50000, 60000]
#~~~~~~~~~~ Tests ~~~~~~~~~~~#



value20k = 20000
value30k = 30000
value40k = 40000
value50k = 50000
value60k = 60000


#~~~~~~~~~~ List Inverted Case ~~~~~~~~~~~#


listInvertedCase20k = listInv(value20k)
listInvertedCase30k = listInv(value30k)
listInvertedCase40k = listInv(value40k)
listInvertedCase50k = listInv(value50k)
listInvertedCase60k = listInv(value60k)



listQuestionInvertedCase = [listInvertedCase20k,listInvertedCase30k,
                            listInvertedCase40k,
                            listInvertedCase50k,listInvertedCase60k]

timeSortInvertedCase = []



#~~~~~~~~~~ Random List Case ~~~~~~~~~~~#


listRandomCase20k = generateList(value20k)
listRandomCase30k = generateList(value30k)
listRandomCase40k = generateList(value40k)
listRandomCase50k = generateList(value50k)
listRandomCase60k = generateList(value60k)




listQuestionRandomCase = [listRandomCase20k,listRandomCase30k,
                          listRandomCase40k,listRandomCase50k,
                          listRandomCase60k] 
timeSortRandomCase = []




for i in range(5):
    timeSortInvertedCase.append(timeit.
                                timeit("radixSort({})".format(listQuestionInvertedCase[i]),
                                              setup="from __main__ import radixSort,countingSort, listInv, generateList",number = 1))
    timeSortRandomCase.append(timeit.
                              timeit("radixSort({})".format(listQuestionRandomCase[i]),
                                            setup="from __main__ import radixSort, countingSort, listInv, generateList",number = 1))
    
    print(i)


drawGraph(listValueGraph,
          timeSortInvertedCase,
          timeSortRandomCase, 
          XAxis="Número de elementos em milhares", 
          YAxis="Tempo de ordenação em Seg",
         name = "Tempo de ordenação em Seg RadixSort com CS")
