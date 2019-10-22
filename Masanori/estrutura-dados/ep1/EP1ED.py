
import time
from random import shuffle



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

def quicksort(v):
    if len(v) <= 1: 
        return v
    
    pivo = v[0]
    iguais  = [x for x in v if x == pivo]
    menores = [x for x in v if x <  pivo]
    maiores = [x for x in v if x >  pivo]
    return quicksort(menores) + iguais + quicksort(maiores)

# Método de ordenação SORT
# CUSTO:  
def selectionSort(v):
  resp = []
  while v:
    m = min(v)
    resp.append(m)
    v.remove(m)
  return resp

# Recebe uma lista de tempos e
# quantas partes deve quebrar
# para que cada linha seja referente a
# um tempo de execução
def split_list(lista, qtdPartes):
    length = len(lista)
    return [ lista[i*length // qtdPartes: (i+1)*length // qtdPartes] 
        for i in range(qtdPartes) ]

def desenhaNaTela(listaTempoGasto, contadorPartes):

    listaNova = split_list(listaTempoGasto, qtdPartes=contadorPartes)
    qtdElementos = 2000

    print('---------------------------------------')
    print('      |    MS    QS     S    N    |')
    for x in range(len(listaNova)):
        print(qtdElementos, " | ", listaNova[x], " |")
        qtdElementos+= 2000
    print('---------------------------------------')
    print('Legenda:')
    print('MS  -  MergeSort - Custo: log2n')
    print('QS  -  QuickSort - Custo: Pior caso - n^2 | Melhor medio caso - log2n')
    print('S   -  Selection - Custo: n^2')
    print('N   -  Native    - Custo: ')

def main():
    rangeList = 2000
    listaTempoGasto = []
    contadorPartes = 0
    while(rangeList <= 20000):
        rangeList += 2000
        # Recebe os numeros e embaralha
        v = list(range(rangeList))
        shuffle(v)

        # inicia o timer para cada tipo
        # de metodo de sort, calcula o tempo
        # e adiciona em um array
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
    desenhaNaTela(listaTempoGasto, contadorPartes)

main()
