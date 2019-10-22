

def enumeracoes(items):
    n = len(items)
    s = [0]*(n+1)
    k = 0
    while True:
        if s[k] < n:
            s[k+1] = s[k] + 1
            k += 1
        else:
            s[k-1] += 1
            k -= 1
        if k == 0:
            break
        else:
            lista = []
            for j in range(1, k+1):
                lista.append(items[s[j]-1])
            yield lista





def combinacoes(items, n):
    if n == 0: yield []
    else:
        for i in range(len(items)):
            for cc in combinacoes(items[:i]+items[i+1:],n-1):
                yield [items[i]]+cc


def permutacoes(items):
    return combinacoes(items, len(items))



def leArquivo(caminhoDoArquivo):
    arquivo = open(caminhoDoArquivo)
    texto = arquivo.readlines()
    aux_d = 0
    dicionario = {}
    for i in texto:
        linha = texto[aux_d].split()
        dicionario[linha[0]] = linha[1:]
        aux_d += 1
    arquivo.close()
    return dicionario



def casamento(damasCavaleiros):
    dama = 0
    while dama < len(damasCavaleiros.keys()):
        if len(damasCavaleiros[damasCavaleiros.keys()[dama]]) == 1:
            if damasCavaleiros[damasCavaleiros.keys()[dama]] == damasCavaleiros[damasCavaleiros.keys()[dama+1]]:
                return 'Preferencia de ' +damasCavaleiros.keys()[dama] + '-'+  damasCavaleiros.keys()[dama + 1] + ' insuficientes e'
        dama+= 1

    for k in enumeracoes(damasCavaleiros.keys()):
        casado = []

        for i in k:
            j = 0
            qtdCavaleiros = len(damasCavaleiros[i])

            if qtdCavaleiros == 0:
                return "Preferencias de " + i + " sao insuficientes e nao e possivel arrumar a mesa e"
            if qtdCavaleiros == 1:
                if damasCavaleiros[i][j] not in casado:
                    casado.append(damasCavaleiros[i][j])
                else:
                    return "Impossivel realizar o casamento!"
            while j < qtdCavaleiros:
                if damasCavaleiros[i][j] not in casado:
                    casado.append(damasCavaleiros[i][j])
                    return ("Casamento possivel e")
                    break
                j += 1


listaCasamento = leArquivo("./casamento.txt")
print(casamento(listaCasamento))

cavaleirosFriends = leArquivo("./cavaleiros.txt")
cavaleiros = cavaleirosFriends.keys()




mesaPossivel = False
for p in permutacoes(cavaleiros):
    resultadoMesa = ''
    if p[1] in cavaleirosFriends[p[0]] and p[2] in cavaleirosFriends[p[1]] \
        and p[3] in cavaleirosFriends[p[2]] and p[4] in cavaleirosFriends[p[3]] \
        and p[5] in cavaleirosFriends[p[4]] and p[6] in cavaleirosFriends[p[5]] \
        and p[0] in cavaleirosFriends[p[6]]:
        mesaPossivel = True
        print("Mesa: %s" % p[0:7])
        break
    else:
        continue


if not mesaPossivel:
    print('Nao eh possivel arrumar a mesa')

