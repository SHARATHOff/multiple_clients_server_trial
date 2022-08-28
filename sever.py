import socket
import threading
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
port = 50000
server.bind((host,port))
server.listen()
clients = []
alises = []
def sendmessage(message):
    for client in clients:
        client.send(message)
def handle_cliens(client):
    while True:
        try:
            message = client.recv(1024)
            sendmessage(message.encode())
        except:
            break
            
def recivingmessage():
    while True:
        print('SERVER IS RUNNING....')
        client , address = server.accept()
        print(f'{address} has connected to the server')
        client.send('alises NAME ?'.encode())
        alise = client.recv(1024)
        alises.append(alise)
        clients.append(client)
        print(f'{alise} is connected to the server')
        sendmessage(f'{alise} is connected to the party'.encode())
        client.send('you are connected '.encode())
        thread = threading.Thread(target=handle_cliens,args=(client,))
        thread.start()


recivingmessage()
def A():
    for i in range(10):
        return i*1