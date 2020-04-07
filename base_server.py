from socket import *

#endereco da porta de comunicacao
minhaPort = 9090

#instanciação do objeto socket, com os parametros de ip e tcp respectivamente
sockobj = socket(AF_INET, SOCK_STREAM)

#o bind faz a conexao do cliente que nesse caso é o nc com a porta de concexao tcp/ip
sockobj.bind(('localhost', minhaPort))
sockobj.listen()

#loop infinito pois um servidor normalmente trabalha sem interrupcoes
while True:
    #o metodo accept aceita a conexao e retorna uma tupla com a conexao e com o endereco ip da maquina conectada 
    conexao, endereco = sockobj.accept()
    while True:
        # recv recebe como parametro o tamanho da palavra 

        data = conexao.recv(1024).decode('utf-8')
        print('Servidor funcionando...')
        
        myString = '> '
        if not data: break
        # o send retorna a mensagem para o cliente 
        conexao.send(myString.encode('utf-8') + data.encode('utf-8'))
        print('{} - {}'.format(endereco, data))
        if data.strip() == "FIM":
            break
    conexao.close()
    print('Esperando novas conexões...')

sockobj.close()
        

