#Lista 1 - 1
a= int(input("digite o primeiro número inteiro:"))
b= int(input("digite o segundo número inteiro:"))
print (a+b)

#Lista 1 - 2
metros = input("digite o valor em metros: ")
metros = int(metros)
milímetros = metros * 1000
milímetros = str(milímetros) + 'mm'
print(milímetros)

#Lista 1 - 3
dia = input('número de dias: ')
dia = int(dia)
hora = input('número de horas: ')
hora = int(hora)
minuto = input('número de minutos: ')
minuto = int(minuto)
segundo = input('número de segundos: ')
segundo = int(segundo)

resultadosegundo = segundo
resultadominuto = minuto*60
resultadohora = hora*60*60
resultadodia = dia*24*3600

print(resultadodia)
print(resultadohora)
print(resultadominuto)
print(resultadosegundo)
print(resultadodia+resultadohora+resultadominuto+resultadosegundo)

#Lista 1 - 4
salário = 1000
aumento=10/100
novo_salário = salário * aumento
print(novo_salário+salário)


#Lista 1 - 5
pão=0.50
desconto=10/100*pão
pão_desconto=pão-desconto
print(desconto)
print(pão_desconto)

#Lista 1 - 6
d = int(input('Qual a distancia: '))
v = int(input('Qual a velocidade: '))
print(v/d)

#Lista 1 - 7
C = int(input('Qual a temperatura em C: '))
F = (9*C/5) + 32
print(F)

#Lista 1 - 8
F = int(input('Qual a temperatura em F: '))
C = 5*(F-32)/9
print(C)

#Lista 1 - 9
km = int(input('km: '))
dias = int(input('dias: '))
preço= km*0.15+dias*60
print('preço: %.2f' %preço)
     
#Lista 1 - 10
dia =  int(input('quantos dias: '))
cigarro = 24*60/10
total = cigarro/144
print('total: ')

#Lista 1 - 11
a=2**1000000
str(a)
print(len(str(a)))
print(len(str(2**1000000)))





     









