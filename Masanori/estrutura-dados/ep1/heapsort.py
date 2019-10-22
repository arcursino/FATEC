def heapsort(v):
    inicio = time.time()

    h = [] 

    for x in v:
        heappush(h, x)
    return [heappop(h) for i in range(len(h))]

    v = sample(range(10), 10)
    print (v)
    v = heapsort(v)
    print (v)
    
    fim = time.time()
    print(fim - inicio)
    print(heapsort)