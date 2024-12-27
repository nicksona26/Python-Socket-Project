#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *
import sys

def http_client(server_host, server_port, filename):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    
    try:
        clientSocket.connect((server_host, server_port))
  
        request_message = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\nConnection: close\r\n\r\n"
        
        clientSocket.sendall(request_message.encode('utf-8'))
        
        response = b""
        while True:
            data = clientSocket.recv(1024)
            if not data:
                break
            response += data
        

        print(response.decode('utf-8'))
    
    except Exception as e:
        print("Error:", e)
    
    finally:
        clientSocket.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: client.py server_host server_port filename")
        sys.exit(1)
    
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    filename = sys.argv[3]
    
    http_client(server_host, server_port, filename)
