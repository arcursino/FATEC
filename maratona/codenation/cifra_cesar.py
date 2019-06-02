TAM_MAX_CH = 26

def recebeModo():
    while True:
        modo = input("Quer Criptografar ou Descriptografar: \n").lower()

        if modo in 'criptografar ou c ou descriptografar ou d'.split(' ou '):
            return modo
        else:
            print("Entre com 'criptografar' ou 'c' ou 'decriptografar' ou 'd'\n")


def recebeChave():
    while True:
        chave = int(input("Entre com o número da chave:\n"))

        if chave <= TAM_MAX_CH:
            return chave
        else:
            print("Digite valor menor ou igual a 26\n")
def geraMsgTraduzida(modo, mensagem, chave):
    global TAM_MAX_CH

    if modo[0] == 'd':
        chave *= -1

    traduzido = ''

    for simbolo in mensagem:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += chave

            if num > ord('z'):
                num -= TAM_MAX_CH
            if num < ord('a'):
                num += TAM_MAX_CH

            traduzido += chr(num)

        else:
            traduzido += simbolo

    return traduzido

def main():

    modo = recebeModo()
    mensagem = input("Entre com sua mensagem: \n")
    chave = recebeChave()


    print('Seu texto traduzido é: ')
    print(geraMsgTraduzida(modo, mensagem, chave))

main()


