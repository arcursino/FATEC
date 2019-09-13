A = [[0, 1, 0, 0, 0, 0], 
     [0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 0],
     [0, 0, 1, 0, 1, 0],
     [1, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0]]

def Distancias(n, origem):
  d = [-1] * n
  d[origem] = 0
  f = []
  f.append(origem)
  while len(f) > 0:
    x = f[0]
    del f[0]
    for y in range(n):
      if A[x][y] == 1 and d[y] == -1:
        d[y] = d[x] + 1
        f.append(y)
  return d
print (Distancias(6, 3))

def quicksort(lista):
    if len(lista) <= 1: 
        return lista
    
    pivô = lista[0]
    iguais  = [x for x in lista if x == pivô]
    menores = [x for x in lista if x <  pivô]
    maiores = [x for x in lista if x >  pivô]
    return quicksort(menores) + \
           iguais + quicksort(maiores)

print (quicksort([2, 7, 0, 3, 4, 9, 8, 1, 5, 6]))

	
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

print (inserção([3, 0, 1, 2, 5, 7, 6, 4]))
print (seleção([3, 0, 1, 2, 5, 7, 6, 4]))

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

print (mergesort([3, 4, 8, 0, 6, 7, 4, 2, 1, 9, 4, 5]))
