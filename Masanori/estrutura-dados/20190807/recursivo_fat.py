def fat(n):
    print (f'Instância: f({n})')
    if n <= 1: return 1
    else:
        print(f'Chamada recursiva: {n} * fat ({n-1})')
        return n * fat(n-1)

print (fat(4))
