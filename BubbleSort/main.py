from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
 
def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista
 
# x = Tempo de ordenação  e o Y = tamanho da lista de numeros
 
def desenhaGrafico(x,y,XAxis = "Lista de Numeros", YAxis = "Tempo de ordenação"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Lista de Numeros")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(YAxis)
    plt.xlabel(XAxis)
    fig.savefig(YAxis)
    plt.show()



def bubbleSort(elementList):
    numberSwap = 0
    swapped = True
    while swapped:
        swapped = False
        lenghtList = len(elementList)
        for i in range (lenghtList - 1): #tamanho da lista    
            if elementList[i] > elementList[i+1] :
                elementList[i], elementList[i+1] = elementList[i+1], elementList[i]
                swapped = True
                numberSwap = numberSwap + 1
        if swapped == False:
            return numberSwap


value1k = 1000
value10k = 10000
value30k = 30000
value60k = 60000
list1k = geraLista(value1k)
list10k = geraLista(value10k)
list30k = geraLista(value30k)
list60k = geraLista(value60k)

listValue = [value1k,value10k,value30k,value60k]
listQuestion = [list1k,list10k,list30k,list60k]
timeSort = []
listNumberSwap = []

for i in range(4):
    timeSort.append(timeit.timeit("bubbleSort({})".format(listQuestion[i]),setup="from __main__ import geraLista,bubbleSort",number = 1))
    listNumberSwap.append(bubbleSort(listQuestion[i]))


desenhaGrafico(listValue,timeSort, XAxis="Número de elementos", YAxis="Tempo de ordenação em Seg")
desenhaGrafico(listValue,listNumberSwap, XAxis="Número de elementos", YAxis="Numero de Trocas")
