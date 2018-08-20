a = int(input('Diga o Lado1: '))
b = int(input('Diga o Lado2: '))
c = int(input('Diga o Lado3: '))

if ((a > b + c) or (b > a + c) or (c > a + b)) or (a == 0 or b == 0 or c == 0):
    print('Valores inválidos para os lados. Não é Triângulo')    
else:
    if a == b and b == c and c == a:
        print('Triângulo equilátero')#lados iguais
    elif a == b or b == c or a == c:
        print('Triângulo isósceles')#2lados iguais
    else:
        print('Triângulo escaleno')#3 lados diferentes
                   
