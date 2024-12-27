from multiprocessing import connection
from socket import AF_INET, SOCK_STREAM, gethostname, gethostbyname
import sys
import socket

serverPort = 4856
serverSocket = socket.socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',4856))
serverSocket.listen(1)


hostname = socket.gethostname()    
ip_address = socket.gethostbyname(hostname)


while True:
    print('Server is up and running')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n".encode())
        connectionSocket.send(outputdata.encode())
        
        connectionSocket.close()
        
    except IOError:
            connectionSocket.send("HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n".encode())
            connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
            connection.close()
            
serverSocket.close()
sys.exit()