entrada = '''1 0 0 1 1 0 1
1 1 0 1 1 1 0
0 0 0 0 0 0 1
1 1 1 0 0 0 1 
0 1 1 0 1 0 1'''



entrada = entrada.split('\n')
esquerda = 0
cima = 0
cont = 0
grupo = []
for item in entrada: grupo.append(item.split(' '))
entrada = grupo
i = 0
j = 0

for i in range(len(grupo)):
    for j in range(len(grupo[0])):
        entrada[i][j] = int(grupo[i][j])

numLinhas = len(entrada)
numColunas = len(entrada[0])
grupoEntrada = [[0]*numColunas for i in range(numLinhas)]

grupos = []
grupos.append(0)

proximoGrupo = 1

x = 0
y = 0
for x in range(numLinhas):
    for y in range(numColunas):
        if(entrada[x][y] == 0): continue
            
        esquerda = 0            
        if (y != 0): esquerda = grupoEntrada[x][y -1]
        esquerda = grupos[esquerda]

        cima = 0
        if(x != 0): cima = grupoEntrada[x - 1][y]
        cima = grupos[cima]

        if(esquerda == 0) and (cima == 0):
            grupoEntrada[x][y] = proximoGrupo
            grupos.append(proximoGrupo)
            proximoGrupo = proximoGrupo + 1
        elif( esquerda != 0) and (cima != 0):
            if(esquerda > cima):
                grupoEntrada[x][y] = cima
                grupos[esquerda] = cima
            else:
                grupoEntrada[x][y] = esquerda
                grupos[cima] = esquerda
        elif(cima == 0):
            grupoEntrada[x][y] = esquerda
        else:
            grupoEntrada[x][y] = cima

cont = 0
i = 1

for i in range(len(grupos)):
    if(i == grupos[i]): cont = cont + 1

for linha in grupoEntrada:
    print(linha)