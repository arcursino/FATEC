m = int(input('Quantos metros quadrados deverá ser pintado: '))
#cobertura = 18 litros / 3 metros quadrados
cobertura = 18/3
tintas = m/cobertura
if int(tintas) != tintas:
    tintas = tintas + 1
tintas = int(tintas)
    
print('Quantos latas de tintas: %d' % (tintas))
preço = tintas*80
print('Qual o preço total R$: %0.2f' % (preço))


