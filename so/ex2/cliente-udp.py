#Cliente UDP
#Importo a biblioteca socket para fazer a conexão
import socket
# Endereco IP do Servidor(obtido através do comando ifconfig no terminal)
SERVER = '192.168.43.229'
# Porta que o Servidor esta escutando
PORT = 5002
#Coloco o retorno da instrução em uma variável
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dest = (SERVER, PORT)
print ('Para sair use CTRL+X\n')
msg = input()
while msg != '\x18':
    udp.sendto (msg.encode(), dest)
    msg = input()
udp.close()