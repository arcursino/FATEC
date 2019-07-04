n = int(input())

numeros = []

for i in range(n):
    num = int(input())
    if num >= 1:
        numeros.append(num)

numeros.sort()

anterior = numeros[0]
faltante = -1

for numero in numeros[1:]:
    if numeros[0] != 1:
        faltante = 1
        break
    if anterior != numero - 1:
        faltante = anterior + 1
        break

    anterior = numero
else:
    faltante = numeros[-1] + 1

print(faltante)
