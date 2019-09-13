#Cliente TCP
#Importo a biblioteca socket para fazer a conexão
import socket
# Endereco IP do Servidor(obtido através do comando ifconfig no terminal)
SERVER = '192.168.43.229'
# Porta que o Servidor esta escutando
PORT = 5002
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (SERVER, PORT)
tcp.connect(dest)
print ('Para sair use CTRL+X\n')
msg = input()
while msg != '\x18':
    tcp.send(msg.encode())
    msg = input()
tcp.close()