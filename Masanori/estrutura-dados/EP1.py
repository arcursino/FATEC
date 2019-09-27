import time
from heapq import heappush, heappop
from random import sample, shuffle

def print_tabela():
    print(seleção, inserção, mergesort, quicksort)


def inserção(v):
    inicio = time.time()

    for j in range(1, len(v)):
        x = v[j]
        i = j - 1
    while i >= 0 and v[i] > x:
        v[i + 1] = v[i]
        i = i - 1
        v[i + 1] = x
    return v

    fim = time.time()
    print(fim - inicio)

    

def seleção(v):
    inicio = time.time()

    resp = []

    while v:
        m = min(v)
        esp.append(m)
        v.remove(m)
    return resp

    fim = time.time()

    print(fim - inicio)

    

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
    inicio = time.time()
    
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)

    fim = time.time()
    print(fim - inicio)
    

def quicksort(lista):
    inicio = time.time()
    
    if len(lista) <= 1: 
        return lista
    
    pivô = lista[0]
    iguais  = [x for x in lista if x == pivô]
    menores = [x for x in lista if x <  pivô]
    maiores = [x for x in lista if x >  pivô]
    return quicksort(menores) + iguais + quicksort(maiores)

    fim = time.time()
    print(fim - inicio)
    


vsorte_nativo = vsn.sort_nativo

def main(inserção, seleção, mergesort, quicksort):
    for i in range(5000, 25000, 5000):
        
        inserção(i)
        seleção(i)
        mergesort(i)
        quicksort(i)
       
        #sort_nativo(i)

    print_tabela()

main()









