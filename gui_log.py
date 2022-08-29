import tkinter
from tkinter import *
import socket
import tkinter
from tkinter import messagebox
from tkinter import *
root = tkinter.Tk()
root.title('Login Page')
root.geometry('600x600')
root.config(bg='purple')
title1 = Label(root,text='Sign in',font=('Arial',70),fg='White',bg='purple').pack()
username = Entry(root,width=20,font=('Arial',20))
password = Entry(root,width=20,font=('Arial',20))
username.pack(padx=50,pady=50)
password.pack(padx=50,pady=50)
def createaccount():
    root1 = Tk()
    root1.geometry('400x400')
    root1.config(bg='purple')
    root1.title('CREATE ACCOUNT')
    sub_title = Label(root1,text='Sign Up',font=('Arial',70),fg='White',bg='purple').pack() 
    new_username = Entry(root1,width=20,font=('Arial',20)).pack(padx=50,pady=50)
    new_password = Entry(root1,width=20,font=('Arial',20)).pack(padx=50,pady=50)
    def adduser():
       deuser.append(new_username)
       depass.append(new_password)
       messagebox.showinfo('Account Created')
       root1.destroy()
    bu = Button(root1,text='Create Account',font=('Arial',20),bg='purple',fg='white',command=adduser)
    bu.pack() 
def checkpass():
    global deuser  
    global depass
    user = username.get()
    paswd = password.get()
    deuser = ['Admin','admin','user']
    depass = ['Admin','admin','123']
    if user not  in deuser:
        messagebox.showinfo('information','username does not exist ')
    elif paswd not in  depass:
        messagebox.showinfo('information','Password wrong ')
    else:
        messagebox.showinfo('information','Login successfull ')
but = Button(root,text='Sign in',font=('Arial',20),bg='purple',fg='white',command=checkpass).pack(padx=60,pady=60)

but1 = Button(root,text='create account',font=('Arial',20),bg='purple',fg='white',command=createaccount).pack(padx=70,pady=70)
root.mainloop()