import socket
import threading
clients = []
n = int(input('ENTER NO OF CLIENTS : '))
a = 0
n = 2
host ='127.0.0.1'  # Standard loopback interface address 
port = 6543        # Port to listen on (non-privileged ports are > 1023)
serv = socket.socket()

serv.bind((host, port))
serv.listen()
while a<n:
    conn,addres = serv.accept()
    clients.append(conn)
    a+=1
print(clients)
def C1():
    global msg2
    while True:
        msg1 = clients[1].recv(1024).decode()
        print(f'message from 2nd client {msg1}')
        try:
            clients[1].send(msg2.encode())
        except:
            pass
def C0():
    global msg2
    while True:
        msg2 = clients[0].recv(1024).decode()
        print('message from first client '.format(msg2))
        try:
            clients[0].send(msg1.encode())
        except:
            pass
        C1()
while True:
    try:
        msg1 = clients[0].recv(1024).decode()
        print(f'message from c1 {msg1}')
        msg2 = clients[1].recv(1024).decode()
        print(f'message from c2 {msg2}')
        clients[0].send(msg2.encode())
        clients[1].send(msg1.encode())
    except:
        break