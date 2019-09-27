
import time
from random import shuffle

def inserção(v):
 for j in range(1, len(v)):
   x = v[j]
   i = j - 1
   while i >= 0 and v[i] > x:
     v[i + 1] = v[i]
     i = i - 1
   v[i + 1] = x
 return v


def seleção(v):
  resp = []
  while v:
    m = min(v)
    resp.append(m)
    v.remove(m)
  return resp

def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

def quicksort(lista):
    if len(lista) <= 1: 
        return lista
    
    pivô = lista[0]
    iguais  = [x for x in lista if x == pivô]
    menores = [x for x in lista if x <  pivô]
    maiores = [x for x in lista if x >  pivô]
    return quicksort(menores) + \
           iguais + quicksort(maiores)


def selectionSort(v):
  resp = []
  while v:
    m = min(v)
    resp.append(m)
    v.remove(m)
  return resp

def busca_sequencial(x, v):
    for i in range(len(v)):
        if v[i] == x:
            return i
    return -1



def split_list(lista, qtdPartes):
    length = len(lista)
    return [ lista[i*length // qtdPartes: (i+1)*length // qtdPartes] 
        for i in range(qtdPartes) ]

def printNaTela(listaTempoGasto, contadorPartes):

    listaNova = split_list(listaTempoGasto, qtdPartes=contadorPartes)
    qtdElementos = 5000

    print('|--------------------------------------[EP1 - Vale a pena ordenar?]------------------------------------------------------|')
    print('| Algoritimo escolhido: Todos                                        Duração dos testes:                                 |')
    print('| Nomes: Caroline F Nunes e Ariana Cursino    - FATEC                                                                    |')
    print('|------------------------------------------------------------------------------------------------------------------------|')
    print('|                          Tempo de Ordenação                                        Tempo de Busca                      |')
    print('|------------------------------------------------------------------------------------------------------------------------|')
    print('|   n   |    Inserção    Seleção     Merge.    Quick.    Nativo   |           Binário                 Sequencial         |')
    print('|------------------------------------------------------------------------------------------------------------------------|')
    for x in range(len(listaNova)):
        print(qtdElementos,"|", listaNova[x], "                                                                                     |")
        qtdElementos+= 5000
    print('|------------------------------------------------------------------------------------------------------------------------|')


def main():
    rangeList = 5000
    listaTempoGasto = []
    contadorPartes = 0
    while(rangeList <= 25000):
        rangeList += 5000


        v = list(range(rangeList))
        shuffle(v)


        t = time.time()
        mergesort(v)
        listaTempoGasto.append(round(time.time() - t,2)) 
        
        t = time.time()
        quicksort(v)
        listaTempoGasto.append(round(time.time() - t,2))
        
        t = time.time()
        selectionSort(v)
        listaTempoGasto.append(round(time.time() - t,2))

        t = time.time()
        sorted(v)
        listaTempoGasto.append(round(time.time() - t,2))

        contadorPartes += 1
    printNaTela(listaTempoGasto, contadorPartes)

main()


    
