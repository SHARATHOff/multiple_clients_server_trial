import socket
import tkinter
from tkinter import *
from tkinter import colorchooser,messagebox
import keyboard , pywhatkit
def color1():
    global bgcolor
    bgcolor = colorchooser.askcolor()
    root.config(bg=bgcolor[1])

def ngrokinfromation():
    pywhatkit.search("https://ngrok.com/download")
def About_US():
    messagebox.showinfo("About Us",'''It was created By high school students''')
def server():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 8080
    address = (host,port)
    s.bind(address)
    s.listen(1)
    conn,addr = s.accept()
    print(addr,'has connected to sever and now online ')
    while 1:
        message = input(str('>>'))
        message = message.encode()
        conn.send(message)
        incomming_message = conn.recv(1024)
        incomming_message  = incomming_message.decode()
        print('client : ',incomming_message )
def client(message):
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = ""
    port = 0
    address = (host,port)
    c.connect(address)    
    while 1 :
        incomming_message = c.recv(1024)
        incomming_message = incomming_message .decode()
        print('host : ',incomming_message )
        #message = input(str('>>'))
        message = message.encode()
        c.send(message)

root = Tk()
root.geometry("400x400")
menubar = Menu(root)
menubar.add_command(label="bgcolor",command=color1)
menubar.add_command(label="ngrok infromation",command=ngrokinfromation)
menubar.add_command(label="About",command=About_US)
root.config(menu=menubar)
root.title("Chat Application")
Label(root,text='''CHAT \nAPPLICATION''',font=('arial',30),justify=CENTER).pack()
Label(root,text="           \n").pack()
menubar = Menu(root)
Button1 = Button(root,text="SERVER",font=("Arial",30),command=server).pack()
Label(root,text="           \n").pack()
Button2 = Button(root,text="CLIENT",font=("Arial",35),command=client).pack()
root.mainloop()
