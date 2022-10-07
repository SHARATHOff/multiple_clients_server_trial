import socket
from tkinter import *
from tkinter import Menu , colorchooser , messagebox

from tkinter import *
from tkinter import Listbox , messagebox
import tkinter
i=1
def recvauto():
    pass
def sendbuttonused():
  global i , incomming_message
  sendmessageget= ""
  b = ""
  sendmessageget = Messagebox.get("1.0",END)
  big.send(sendmessageget.encode())
 
 #  listbox1.insert(1,"DSa")
  sendbox.insert(i,f"Me: {sendmessageget}")

  
  
  i+=1
def chatgui():
    #global Messagebox, sendbox,recvbox
    gui = Tk()
    gui.geometry("500x550")
    gui.resizable(False,False)
    frame1 = LabelFrame(gui,text="   Chatting Area - Serverside",font=("Arial",20),padx=5,pady=5)
    frame1.pack(side=TOP)
    frame2 = Frame(gui)
    frame2.pack(side=BOTTOM)
    recvbox = Listbox(frame1,width=30,height=25,justify=LEFT)
    recvbox.pack(side=LEFT,padx=0,pady=0)
    sendbox = Listbox(frame1,width=30,height=25,justify=RIGHT)
    sendbox.pack(side=RIGHT)
    Messagebox = Text(frame2,font=("arial"),height=4,width=30)
    Messagebox.pack(side=LEFT)
    sendbutton = Button(frame2,text="ENTER",height=3,width=15,command=sendbuttonused)
    sendbutton.pack(side=RIGHT)
    gui.mainloop()


def gethostprt():
    global host
    global port
    host = hostlabel.get()
    port = portlabel.get()
    port = int(port)
    #print(port)
def color1():
    global bgcolor
    bgcolor = colorchooser.askcolor()[1]
    print(bgcolor)
    root.config(bg=bgcolor)
def ngrokinfromation():
    pass
    pywhatkit.search("https://ngrok.com/download")
def About_US():
    messagebox.showinfo("About Us",'''It was created By high school students''')
# global root ,l1,l2
def chatting():
    global host , port , clientserver , Messagebox,sendbox,recvbox , incomign,big
    clientserver = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address = (host,port)
    clientserver.connect(address)
    gui = Tk()
    gui.geometry("500x550")
    gui.resizable(False,False)
    frame1 = LabelFrame(gui,text="   Chatting Area - Serverside",font=("Arial",20),padx=5,pady=5)
    frame1.pack(side=TOP)
    frame2 = Frame(gui)
    frame2.pack(side=BOTTOM)
    recvbox = Listbox(frame1,width=30,height=25,justify=LEFT)
    recvbox.pack(side=LEFT,padx=0,pady=0)
    sendbox = Listbox(frame1,width=30,height=25,justify=RIGHT)
    sendbox.pack(side=RIGHT)
    Messagebox = Text(frame2,font=("arial"),height=4,width=30)
    Messagebox.pack(side=LEFT)
    sendbutton = Button(frame2,text="ENTER",height=3,width=15,command=sendbuttonused)
    sendbutton.pack(side=RIGHT)
    i=1
    #while True:
    print("SAD")
    incomign = big.recv(1024).decode()
    recvbox.insert(i,f"client : {incomign}")
    i+=1

    gui.mainloop()
    print("success")
class Mainserver():
    def clientconnector():

        global hostlabel
        global portlabel
        root.destroy()
        gui1 = Tk()
        gui1.geometry("300x320")
        gui1.resizable(False,False)
        Label(gui1,text="Connecting......",font=("arial",30)).pack(side=TOP)
        connectbutton = Button(gui1,text="Connect",font=("arial",20),command=lambda:[gethostprt(),gui1.destroy(),chatting()])
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
Button2 = Button(root,text="CLIENT",font=("Arial",35),command=lambda :[Mainserver.clientconnector()]).pack()
root.mainloop()

	
