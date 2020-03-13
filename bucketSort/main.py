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



  
def bucketSortWithCountingSort(array):
    code = hashing(array)
    buckets = [list() for _ in range( code[1] )]
    for i in array:
        x = re_hashing( i, code )
        buck = buckets[x]
        buck.append( i )
    for bucket in buckets:
        countingSort(bucket)
         
    ndx = 0
    for b in range( len( buckets ) ):
        for v in buckets[b]:
            array[ndx] = v
            ndx += 1
    
    return array



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

#~~~~~~~~~~BucketSort with quickSort~~~~~~~~~~#

def bucketSortWithQuickSort(array):
    code = hashing(array)
    buckets = [list() for _ in range( code[1] )]
    for i in array:
        x = re_hashing( i, code )
        buck = buckets[x]
        buck.append( i )
    for bucket in buckets:
        startingQuickSort(bucket)
         
    ndx = 0
    for b in range( len( buckets ) ):
        for v in buckets[b]:
            array[ndx] = v
            ndx += 1
    
    return array

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
        
def startingQuickSort(newList):
  quickSort(newList, 0, len(newList) -1)
  
  
#~~~~~~~~~~~~BucketSort with mergeSort~~~~~~~~~~~#

def bucketSortWithMergeSort(array):
    code = hashing(array)
    buckets = [list() for _ in range( code[1] )]
    for i in array:
        x = re_hashing( i, code )
        buck = buckets[x]
        buck.append( i )
    for bucket in buckets:
        startingMergeSort(bucket)
         
    ndx = 0
    for b in range( len( buckets ) ):
        for v in buckets[b]:
            array[ndx] = v
            ndx += 1
    
    return array

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

      
def hashing(array):
    m = array[0]
    for i in range(1, len(array)):
        if ( m < array[i] ):
            m = array[i]
    result = [m,int(math.sqrt( len(array)))]
    return result

  
def re_hashing(i, code ):
    return int(i/code[0]*(code[1]-1))      
      
      
def listInv(tamanho):
  lista =[]
  for i in range(tamanho, 0, -1):
    lista.append(tamanho)
    tamanho = tamanho - 1
  return lista


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



listValueGraph = [15000,25000,35000,45000,55000]
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


listInvertedQS15k = listInvertedCase15k
listInvertedQS25k = listInvertedCase25k
listInvertedQS35k = listInvertedCase35k
listInvertedQS45k = listInvertedCase45k
listInvertedQS55k = listInvertedCase55k 


listInvertedMS15k = listInvertedCase15k
listInvertedMS25k = listInvertedCase25k
listInvertedMS35k = listInvertedCase35k
listInvertedMS45k = listInvertedCase45k
listInvertedMS55k = listInvertedCase55k 



listQuestionInvertedCase = [listInvertedCase15k,listInvertedCase25k,
                            listInvertedCase35k,listInvertedCase45k,
                            listInvertedCase55k]

timeSortInvertedCase = []

listQuestionInvertedQS = [listInvertedQS15k,listInvertedQS25k,
                            listInvertedQS35k,listInvertedQS45k,
                            listInvertedQS55k]
timeSortInvertedQS = []

listQuestionInvertedMS = [listInvertedMS15k,listInvertedMS25k,
                            listInvertedMS35k,listInvertedMS45k,
                            listInvertedMS55k]
timeSortInvertedMS = []

#~~~~~~~~~~ Random List Case ~~~~~~~~~~~#

listRandomCase15k = generateList(value15k)
listRandomCase25k = generateList(value25k)
listRandomCase35k = generateList(value35k)
listRandomCase45k = generateList(value45k)
listRandomCase55k = generateList(value55k)


listRandomQS15k = listRandomCase15k
listRandomQS25k = listRandomCase25k
listRandomQS35k = listRandomCase35k
listRandomQS45k = listRandomCase45k
listRandomQS55k = listRandomCase55k 


listRandomMS15k = listRandomCase15k
listRandomMS25k = listRandomCase25k
listRandomMS35k = listRandomCase35k
listRandomMS45k = listRandomCase45k
listRandomMS55k = listRandomCase55k 



listQuestionRandomCase = [listRandomCase15k,listRandomCase25k,
                          listRandomCase35k,listRandomCase45k,
                          listRandomCase55k] 
timeSortRandomCase = []

listQuestionRandomQS = [listRandomQS15k,listRandomQS25k,
                          listRandomQS35k,listRandomQS45k,
                          listRandomQS55k]
timeSortRandomQS = []

listQuestionRandomMS = [listRandomMS15k,listRandomMS25k,
                          listRandomMS35k,listRandomMS45k,
                          listRandomMS55k]
timeSortRandomMS = []

for i in range(5):
    timeSortInvertedCase.append(timeit.
                                timeit("bucketSortWithCountingSort({})".format(listQuestionInvertedCase[i]),
                                              setup="from __main__ import bucketSortWithCountingSort,countingSort, listInv, generateList",number = 1))
    timeSortRandomCase.append(timeit.
                              timeit("bucketSortWithCountingSort({})".format(listQuestionRandomCase[i]),
                                            setup="from __main__ import bucketSortWithCountingSort, countingSort, listInv, generateList",number = 1))
    timeSortInvertedQS.append(timeit.
                                timeit("bucketSortWithQuickSort({})".format(listQuestionInvertedQS[i]),
                                              setup="from __main__ import bucketSortWithQuickSort, startingQuickSort, quickSort,partitionForQuickSort, listInv, generateList",number = 1))
    timeSortRandomQS.append(timeit.
                              timeit("bucketSortWithQuickSort({})".format(listQuestionRandomQS[i]),
                                            setup="from __main__ import bucketSortWithQuickSort, startingQuickSort, quickSort,partitionForQuickSort, listInv, generateList",number = 1))
    timeSortInvertedMS.append(timeit.
                                timeit("bucketSortWithMergeSort({})".format(listQuestionInvertedMS[i]),
                                              setup="from __main__ import bucketSortWithMergeSort,startingMergeSort,mergeSort,merging, listInv, generateList",number = 1))
    timeSortRandomMS.append(timeit.
                              timeit("bucketSortWithMergeSort({})".format(listQuestionRandomMS[i]),
                                            setup="from __main__ import bucketSortWithMergeSort, startingMergeSort,mergeSort,merging, listInv, generateList",number = 1))
    
    print(i)

drawGraph(listValueGraph,
          timeSortInvertedCase,
          timeSortRandomCase, 
          XAxis="Número de elementos em milhares", 
          YAxis="Tempo de ordenação em Seg",
         name = "Tempo de ordenação em Seg BucketSort com CS")

drawGraph(listValueGraph,
          timeSortInvertedQS,
          timeSortRandomQS, 
          XAxis="Número de elementos em milhares", 
          YAxis="Tempo de ordenação em Seg",
         name = "Tempo de ordenação em Seg BucketSort com QS")

drawGraph(listValueGraph,
          timeSortInvertedMS,
          timeSortRandomMS, 
          XAxis="Número de elementos em milhares", 
          YAxis="Tempo de ordenação em Seg",
         name = "Tempo de ordenação em Seg BucketSort com MS")
