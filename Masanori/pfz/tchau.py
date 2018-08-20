m = int(input('Quantos minutos a madame falou: '))
if m < 200:
    print(m*0.20)
if m >= 200 and m <= 400:
    print(m*0.18)
else:
    print(m*0.15)
