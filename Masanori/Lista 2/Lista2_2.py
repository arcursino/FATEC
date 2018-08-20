ano = int(input('Qual o ano: '))
if ano % 4 == 0 and (ano % 100 != 0 or ano %400 == 0):
    print('Ano Bissexto')
else:
    print('Não é ano Bissexto')
    





# return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)



