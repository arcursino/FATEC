minutos = int(input('Quantos minutos você falou?: '))
if minutos < 200:
    preço = 0.20
else:
    if minutos <=400:
        preço = 0.18
    else:
        preço = 0.15
total = minutos*preço
print ('Valor da conta: R$ %06.2f' %(minutos*preço))
print ('Valor da conta: R$%3.4f' %total)



              
