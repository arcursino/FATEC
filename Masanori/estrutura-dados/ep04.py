f = open(r’ariana@arcursino:~/Downloads/ESCOLA.CSV’)
s = open(r’ariana@arcursino:~/Downloads/s.csv, 'w')
rotulos = f.readline().split(‘|’)
s.write(campos[4] + '\n')

print (rotulos[4])

for campos in f:
    campos = campos.split(‘|’)
    s.write(campos[4] + '\n')

f.close()
s.close()