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



#print(type(dia))

















