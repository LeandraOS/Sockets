from socket import *

host_servidor = ''
porta_servidor = 9090
socketobj = socket(AF_INET, SOCK_STREAM)
socketobj.connect((serverHost, serverPort))

while True:
    mensagem = input("Você: ")
    socketobj.send(msg.encode('utf-8'))

    dados = socketobj.recv(1024)
    print('Ele: ', dados.decode('utf-8'))
    if dados.strip == 'BYE':
        socketobj.close()