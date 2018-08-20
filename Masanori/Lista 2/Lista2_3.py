p = int(input('Quantos quilos de peixes: '))
if p >= 50:
    excedente = p -50
    multa = (excedente*4)
    print('o valor da multa R$: %0.2f' % (multa))
else:
    print('Conteúdo Zero')
    
