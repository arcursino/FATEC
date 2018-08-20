m = int(input('Quantos minutos a madame falou: '))
if m<200:
    preço = 0.20
else:
    if m>= 200 and m<400:
        preço = 0.18
    else:
        preço = 0.15

print('A conta da madame deu R$: %0.2f' % (m*preço))


        
