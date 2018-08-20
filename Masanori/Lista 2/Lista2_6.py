hora = int(input('Quantos você ganha por hora: '))
mês = int(input('Quantas horas você trabalha por mês: '))
Bruto = hora * mês
IR = Bruto * 0.11
INSS = Bruto * 0.08
Sindicato = Bruto * 0.05
Líquido = Bruto - IR - INSS - Sindicato 
print('Salário Bruto é: %0.2f' % (Bruto))
print('Desconto do Imposto de Renda é: %0.2f' % (IR))
print('INSS é: %0.2f' % (INSS))
print('Sindicato é: %0.2f' %(Sindicato))
print('O Salário líquido é: %0.2f' % (Líquido))




