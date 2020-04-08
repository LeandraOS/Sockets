from socket import *
from threading import Thread

def servidor(conexao, endereco):
    while True:
        mensagem = conexao.recv(1024).decode('utf-8')
        
        myString = '> '
        if not mensagem: break
        conexao.send(myString.encode('utf-8') + mensagem.encode('utf-8'))
        print('{} - {}'.format(endereco, mensagem))
        if mensagem.strip() == "FIM":
            break
    conexao.close()
    print('Cliente {} desconectado! Esperando novas conexões...'.format(endereco[1]))

def executa():
    minhaPorta = 9090
    socketobj = socket(AF_INET, SOCK_STREAM)
    socketobj.bind(('localhost', minhaPorta))
    socketobj.listen()
    print('Servidor funcionando...\n')
    while True:
        conexao, endereco = socketobj.accept()
        print('Conexão aceita de {} : {}'.format(endereco[0], endereco[1]))
        Thread(target=servidor, args=(conexao, endereco)).start()

    socketobj.close()

executa()


