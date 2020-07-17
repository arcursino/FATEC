centavos = int(input())
moedas = int(input())

moedas_array = []
for _ in range(moedas):
    moedas_array.append(int(input()))
    
    
def soma_elementos(n):
    total = 0
    for i in n:
       soma = total + i
    return soma
   
def fatorial(n):
    if n<=1:
        return 1
    else:
        return n*fatorial(n-1) 
    
while(soma_elementos(moedas_array) <= centavos):
    count = 0
    for i in moedas_array:
        total = fatorial(centavos) / (fatorial(centavos - moedas) * fatorial(moedas)) 
        count += 1  
  
print(int(count))