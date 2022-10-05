from socket import *
#serverName = ''
serverName = gethostname()
serverPort = 12000
while 1:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    sentence = input('Input lowercase sentence:').encode()

    if not sentence:
        break

    clientSocket.send(sentence)
    modifiedSentence = clientSocket.recv(1024)
    mensagemCodificada = modifiedSentence.decode('utf-8')
    result = f'{mensagemCodificada}'
    print ('From Server:', mensagemCodificada)
    clientSocket.close()


clientSocket.close()
