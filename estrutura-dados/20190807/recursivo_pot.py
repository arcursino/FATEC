def pot(x, n):
    print (f'Instância: pot({x}, {n})')
    if n == 0: return 1
    else:
        print(f'Chamada recursiva: {x}* pot({x}, {n-1})')
        return x * pot(x, n-1)
print (pot(2, 3))
    
