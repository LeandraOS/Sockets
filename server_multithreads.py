from socket import *
from threading import Thread

def servidor(conexao, endereco):
    while True:
        data = conexao.recv(1024).decode('utf-8')
        
        myString = '> '
        if not data: break
        conexao.send(myString.encode('utf-8') + data.encode('utf-8'))
        print('{} - {}'.format(endereco, data))
        if data.strip() == "FIM":
            break
    conexao.close()
    print('Esperando novas conexões...')



def executa():
    minhaPort = 9090
    sockobj = socket(AF_INET, SOCK_STREAM)
    sockobj.bind(('localhost', minhaPort))
    sockobj.listen()
    print('Servidor funcionando...\n')
    while True:
        conexao, endereco = sockobj.accept()
        print('Conexão aceita de {} : {}'.format(endereco[0], endereco[1]))
        Thread(target=servidor, args=(conexao, endereco)).start()

    sockobj.close()

executa()


