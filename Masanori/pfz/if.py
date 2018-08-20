Velocidade = int(input('Qual a velocidade do carro: '))
if Velocidade > 110:
    print ('Você foi multado!')
    multa = (Velocidade-110)*5
    print ('Valor da multa: R$ %5.2f' %multa)
else:
    print ('Você está dentro da Lei!')
