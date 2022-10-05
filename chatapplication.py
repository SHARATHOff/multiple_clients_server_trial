import socket
import tkinter , time
from tkinter import *
from tkinter import colorchooser,messagebox,Listbox
from PIL import Image,ImageTk
import keyboard , pywhatkit 
def color1():
    global bgcolor
    bgcolor = colorchooser.askcolor()[1]
    print(bgcolor)
    root.config(bg=bgcolor)
    l1.config(bg=bgcolor)
   #@ root1.config(bg=bgcolor)

def ngrokinfromation():
    pass
    pywhatkit.search("https://ngrok.com/download")
def About_US():
    messagebox.showinfo("About Us",'''It was created By high school students''')
def server():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = "localhost"
    port = 8080
    address = (host,port)
    s.bind(address)
    s.listen(1)
    print("listing")
    conn,addr = s.accept()
    print(addr,'has connected to sever and now online ')
    while 1:
        message = input(str('>>'))
        message = message.encode()
        conn.send(message)
        incomming_message = conn.recv(1024)
        incomming_message  = incomming_message.decode()
        print('client : ',incomming_message )
def gethostprt():
    global host
    global port
    host = hostlabel.get()
    port = portlabel.get()
    port = int(port)

def clientconnector():
    global hostlabel
    global portlabel
    root.destroy()
    gui1 = Tk()
    gui1.geometry("300x320")
    gui1.resizable(False,False)
    Label(gui1,text="Connecting......",font=("arial",30)).pack(side=TOP)
    connectbutton = Button(gui1,text="Connect",font=("arial",20),command=lambda:[gethostprt(),gui1.destroy()])
    connectbutton.pack(side=BOTTOM)
    clientgui = Frame(gui1)
    clientgui.pack(side=LEFT)
    Label(clientgui,text="HOST ",justify=CENTER,font=("arail",20)).pack()
    Label(clientgui,text="",justify=CENTER).pack()
    Label(clientgui,text="PORT ",justify=CENTER,font=("arail",20)).pack()
    clientgui2 = Frame(gui1)
    clientgui2.pack(side=RIGHT)
    hostlabel = Entry(clientgui2,width=15,font=("arial",20))
    hostlabel.pack()
    Label(clientgui2,text="",justify=CENTER).pack()
    portlabel = Entry(clientgui2,width=15,font=("arail",20))
    portlabel.pack()
    buttonframe = Frame(gui1)
    buttonframe.pack(side=BOTTOM)
    #Label(clientgui2,text="",justify=CENTER).pack()
    clientgui.mainloop()
    client()

def client():
    host1 = host
    port1 = port
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address = (host1,port1)
    c.connect(address)   
    print(address) 
    while 1 :
        incomming_message = c.recv(1024)
        incomming_message = incomming_message .decode()
        print('host : ',incomming_message )
        message = input(str('>>'))
        message = message.encode()
        c.send(message)
def server_messager():
    pass
class Myclass():
    def __init__(self):
         self.root = Tk()
         self.root.geometry("400x400")
         menubar = Menu(self.root)
         menubar.add_command(label="bgcolor",command=color1)
         menubar.add_command(label="ngrok infromation",command=ngrokinfromation)
         menubar.add_command(label="About",command=About_US)
         self.root.config(menu=menubar)
         self.root.title("Chat Application")
         Label(self.root,text='''CHAT \nAPPLICATION''',font=('arial',30),justify=CENTER).pack()
         Label(self.root,text="           \n").pack()
         menubar = Menu(self.root)
         Button1 = Button(self.root,text="SERVER",font=("Arial",30),command=server).pack()
         Label(self.root,text="           \n").pack()
         Button2 = Button(self.root,text="CLIENT",font=("Arial",35),borderwidth=1,command=client).pack()
def globalorlocal():
    messagebox.showinfo("Infromation",'''       HOW TO CONFIG NGROK TO THE SERVER \nstep 1: download ngrok from you browser\nstep 2: Run the downloaded file\nstep 3:	connect you ngrok account to the ngrok terminal\nstep 4: Run this command "ngrok tcp 8080" \nstep 5: extract the host and port from the forward url like this\n	"tcp://0.tcp.in.ngrok.io:18088"\n now set the host = "0.tcp.in.ngrok.io"\nthen port = 18088\nnow ,ask client to enter the host and port number on the dialog box ''')
    server()
def main1():
    global root ,l1,l2
    root = Tk()
    root.geometry("400x400")
    root.resizable(False,False)
    menubar = Menu(root)
    menubar.add_command(label="bgcolor",command=color1)
    menubar.add_command(label="ngrok infromation",command=ngrokinfromation)
    menubar.add_command(label="About",command=About_US)
    root.config(menu=menubar)
    root.title("Chat Application")
   # bgimage = ImageTk.PhotoImage(Image.open(r"C:\Users\JOKER\Documents\Python_Projects\Programming\clienttoclient sever\a1.jpg"))
  #  Label(root,image=bgimage,width=400,height=400).pack()
    l1 = Label(root,text='''CHAT \nAPPLICATION''',font=('arial',30),justify=CENTER).pack()
    l2 = Label(root,text="           \n").pack()
    menubar = Menu(root)
    Button1 = Button(root,text="SERVER",font=("Arial",30),command=lambda :[globalorlocal()]).pack()
    Label(root,text="           \n").pack()
    Button2 = Button(root,text="CLIENT",font=("Arial",35),command=lambda :[clientconnector()]).pack()
    root.mainloop()
main1()


