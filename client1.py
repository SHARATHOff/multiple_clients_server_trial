import socket

host = '127.0.0.1'  # Standard loopback interface address         

port = 6543        # Port to listen on (non-privileged ports are > 1023)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


while True:
    message = input("Message")
    client.send(message.encode())
    try:
        inmessa = client.recv(1024).decode()
        print(f'Message form another client {inmessa}')
    except:
        pass