m = int(input('Quantos minutos a madame falou: '))
if m < 200:
    preço = 0.20
elif m >= 200:
    preço = 0.18
elif m <400:
    preço = 0.18
elif m > 400:
    preço = 0.15
if m > 800:
    preço = 0.08
print('Valor da conta da madame: %0.2f' % (m*preço))

