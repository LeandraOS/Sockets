from socket import *

#endereco da porta de comunicacao
minhaPorta = 9090

#instanciação do objeto socket, com os parametros de endereço ip e de transferencia tcp respectivamente
socketobj = socket(AF_INET, SOCK_STREAM)

#o bind faz a conexao do cliente que nesse caso é o nc com a porta de conexao tcp/ip
socketobj.bind(('localhost', minhaPorta))
socketobj.listen()

#loop infinito pois um servidor normalmente trabalha sem interrupcoes
while True:
    #o metodo accept aceita a conexao direta com o cliente e retorna uma tupla com a conexao e com o endereco ip da maquina conectada 
    conexao, endereco = socketobj.accept()
    while True:
        # recv recebe como parametro o tamanho da palavra 
        mensagem = conexao.recv(1024).decode('utf-8')
        print('Servidor funcionando...')
        
        myString = '> '
        if not mensagem: break
        # o send retorna a mensagem para o cliente 
        conexao.send(myString.encode('utf-8') + mensagem.encode('utf-8'))
        print('{} - {}'.format(endereco, mensagem))
        if mensagem.strip() == "FIM":
            break
    conexao.close()
    print('Cliente {} desconectado! Esperando novas conexões...'.format(endereco[1]))

socketobj.close()