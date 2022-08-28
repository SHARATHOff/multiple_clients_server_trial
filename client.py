import socket
import threading
alise = input('choose you alises : ')

host = '127.0.0.1'
port = 50000
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))
def recivingmessage():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == 'alises NAME ?':
                client.send(alise.encode())
            else:
                print(message)
        except:
            print('Error')
            break
def sendingmessage():
    while True:
        message =  f'{alise} : {input(">>")}'
        client.send(message.encode())
recvthreading = threading.Thread(target=recivingmessage)
recvthreading.start()
sendthreading = threading.Thread(target=sendingmessage)
sendthreading.start()
