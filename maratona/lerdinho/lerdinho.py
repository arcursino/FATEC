busca = input()
quant = int(input())
nomes = []
indice_nome_encontrado = []


for x in range(quant):
    nome, sobrenome = input().split()
    nomes.append([nome, sobrenome])

for i, nome in enumerate(nomes):
    for x in range(len(busca)):
        primeiraparte = busca[:x]
        segundaparte = busca[x:]

        if primeiraparte == "":
            if nome[0].startswith(segundaparte) or nome[1].startswith(segundaparte):
                indice_nome_encontrado.append(i)
                break
        else:
            if nome[0].startswith(primeiraparte) and nome[1].startswith(segundaparte):
                indice_nome_encontrado.append(i)
                break

print(len(indice_nome_encontrado))

for i in indice_nome_encontrado:
    print(" ".join(nomes[i]))



