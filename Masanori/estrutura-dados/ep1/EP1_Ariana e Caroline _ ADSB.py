
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


def selectionSort(v):                             #Método de ordenação
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

cont = 0
def busca_binaria(x, v):
  global cont
  e = -1
  d = len(v)
  while e < d-1:
    m = (e + d) // 2
    cont = cont + 1
    if v[m] < x:
      e = m
    else:
      d = m
  return d

v = list(range(1000000))
from random import randint


def split_list(lista, qtdPartes):
    length = len(lista)
    return [ lista[i*length // qtdPartes: (i+1)*length // qtdPartes] 
        for i in range(qtdPartes) ]

def printNaTela(listaTempoGasto, contadorPartes):

    listaNova = split_list(listaTempoGasto, qtdPartes=contadorPartes)
    qtdElementos = 5000

    print('|--------------------------------------[EP1 - Vale a pena ordenar?]------------------------------------------------------|')
    print('| Algortimo escolhido: Todos                                         Duração dos testes:                                 |')
    print('| Nomes: Caroline F Nunes e Ariana Cursino    - FATEC                                                                    |')
    print('|------------------------------------------------------------------------------------------------------------------------|')
    print('|                          Tempo de Ordenação                                        Tempo de Busca                      |')
    print('|------------------------------------------------------------------------------------------------------------------------|')
    print('|   n   |   Inserção   Seleção    Merge   Quick    Nativo   |  Inserção    Seleção     Merge     Quick     Nativo        |')
    print('|------------------------------------------------------------------------------------------------------------------------|')
    for x in range(len(listaNova)):
        print(qtdElementos,"|", listaNova[x], "                                                                                     |")
        qtdElementos+= 5000
    print('|------------------------------------------------------------------------------------------------------------------------|')


def main():
    rangeList = 5000
    listaTempoGasto = []
    contadorPartes = 0

    t = time.time()
    v = list(range(rangeList))
    busca_sequencial(345,(v))
    listaTempoGasto.append(round(time.time() - t,2))
    
    while(rangeList <= 25000):
        v = list(range(rangeList))        
        shuffle(v)                                              #Recebe os números e embaralha

        t = time.time()                                         
        inserção(list(v))
        listaTempoGasto.append(round(time.time() - t,2))        #Inicia o timer para cada tipo de método de sort 

        t = time.time()
        selectionSort(list(v))
        listaTempoGasto.append(round(time.time() - t,2))

        t = time.time()
        mergesort(list(v))
        listaTempoGasto.append(round(time.time() - t,2)) 
        
        t = time.time()
        quicksort(list(v))
        listaTempoGasto.append(round(time.time() - t,2))
        
        t = time.time()
        sorted(list(v))
        listaTempoGasto.append(round(time.time() - t,2))

        contadorPartes += 1
        rangeList += 5000

        t = time.time()
        busca_binaria(2345,(v))
        listaTempoGasto.append(round(time.time() - t,2))   

    printNaTela(listaTempoGasto, contadorPartes)

main()

# tenho que fazer uma busca sequencial de um elemento fora do while e fazer do mesmo elemento dentro do while, depois de ordenar e comparar...
# para ver se compensa.
# usar o tempo(soma da ordenação mais busca binária) ou até 30 segundos.
# acredito que o contador não precisaremos usar... pelo que pude entender do enunciado.


#Percorrer a lista toda variando o índice i de 0 a len(seq)-1 e comparando cada elemento seq[i] com x. 
# def busca_sequencial( seq, x):
#    '''(list, float) -> bool'''
#    for i in range(len(seq)):
#        if seq[i] == x:
#            return True
#   return False

#def busca_binaria(seq, x):
#   ''' (list, float) -> bool
#        retorna a posicao em que x ocorre na lista ordenada,
#        ou None caso contrario, usando o algoritmo de busca binaria.
#        '''





    
