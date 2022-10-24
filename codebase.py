import socket
import time
import os 
bufsize = 50000
clients_name = []
class Main():
    def __init__(self):
        print("DATA Transfer")
        print("")
        while True:
            print('''SEND OR RECEIVE DATA
            [1] Send 
            [2] Receive
            [3] Exit''')
            snedorrecive = input(("SEND OR RECEIVE DATA : "))
            if snedorrecive=='1':
                Main.send_file_name()
            elif snedorrecive=='2':
                Main.recv_filename()
                pass
            elif snedorrecive=='3':
                exit()
            else:
                continue
                print('Enter the correct one')
    def send_file_name():
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host = "localhost"
        port = 8080
        address = (host,port)
        try:
            print(f'''[HOST] : {host}   
[PORT] : {port}
You can Also use [NGROK] to Tranfer Globally''')
            server.bind(address)
            server.listen()
            client,addr = server.accept()
        except:
            print("sorry...error...")
            exit()
        while True:
            
            print('''Types for Transfer Avilable
            [1] Image Tranfer 
            [2] Video Transfer
            [3] Audio Transfer
            [4] Exit''')
            transfer = input("select your Transfer : ")
            if transfer=="1":
                print("Enter Your File path")
                path = input("full path : ")
                file = open(path,"rb")
                data = file.read()
                client.send(data)
                break
            elif transfer=="2":
                print("Enter Your File path")
                path = input("full path : ")
                file = open(path,"rb")
                data = file.read()
                client.send(data)
                break
            elif transfer=="3":
                print("Enter Your File path")
                path = input("full path : ")
                file = open(path,"rb")
                data = file.read()
                client.send(data)
                break
            elif transfer=="4":
                exit()
            else :
                print("try again")
                continue
    def recv_filename(): 
    
        client_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        while True:
            host = input("ENTER THE HOST ID : ")
            port = int(input("ENTER THE PORT NUMBER : "))
            address = (host,port)
            try: 
                client_server.connect(address)
                break
            except:
                print("host or port is wrong")
                continue
        while True:
            print('''Types for Transfer Avilable
            [1] Image Tranfer 
            [2] Video Transfer
            [3] Audio Transfer
            [4] Exit''')
            transfer = input("select your Transfer : ")
            if transfer=="1":
                print("Enter Your File path to be stored")
                path = input("full path : ")
                file = open(path,"wb")
                data = client_server.recv(bufsize)
                file.write(data)
                file.close()
                break
            elif transfer=="2":
                print("Enter Your File path")
                path = input("full path : ")
                file = open(path,"wb")
                data = client_server.recv(bufsize)
                file.write(data)
                file.close()
                break
            elif transfer=="3":
                print("Enter Your File path")
                path = input("full path : ")
                file = open(path,"wb")
                data = client_server.recv(bufsize)
                file.write(data)
                file.close()
                break
            elif transfer=="4":
                exit()

            else :
                print("try again")
                continue
if __name__=="__main__":
    Main()
    
