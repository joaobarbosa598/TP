from socket import *
serverName = gethostname()
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while 1:
    message = input('Input lowercase sentence:').encode()

    if not message:
        break

    clientSocket.sendto(message, (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    mensagemFinal = modifiedMessage.decode('utf-8')
    result = f'{mensagemFinal}'
    print(result)


clientSocket.close()