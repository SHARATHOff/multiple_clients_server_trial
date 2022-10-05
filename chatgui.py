from tkinter import *
from tkinter import Listbox
import tkinter
i=1
def sendbuttonused():
  global i
  a = ""
  b= ""
  a = Messagebox.get("1.0",END)
  b = Messagebox.get("1.0",END)
 #  listbox1.insert(1,"DSa")
  sendbox.insert(i,f"Client : {a}")
  recvbox.insert(i,f"Me : {b}")
  i+=1
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