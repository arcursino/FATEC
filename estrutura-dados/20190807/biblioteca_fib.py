f = {}
def fib(n):
    if n == 0 or n == 1: return n
    else:
        if n not in f: f[n] = (fib(n - 1) + fib(n - 2))
        return f[n]
    
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    print (f'fib({n})')
    if n <= 2: return 1
    else:(fib(n - 1) + fib(n - 2))
       
    
print(fib(60))
        
