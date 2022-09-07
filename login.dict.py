"""
Login-程式內dict版
作者:Cheng Hong Wu
08/26
Ver.2
可自行修改為使用 SQL or File的使用者資料庫
"""
# dict 使用者資料庫
userdata = {
    "ID":["user","eden","Ted"],
    "PW":["0000","1234","5678"]
}

from tkinter import Tk
from tkinter import Label
from tkinter import StringVar
from tkinter import Entry
from tkinter import Button
def Login():
    def command():
        t = None
        if str(textAccount.get()) in userdata["ID"]:
            t = userdata["ID"].index(str(textAccount.get()))
            if str(textPassword.get()) == userdata["PW"][t]:
                Note.set(f"Welcome! {textAccount.get()} !")
                noteLine.config(fg="green")
                win.destroy()
            else:
                Note.set("※Your Account or Password "
                         "\nis wrong! Please try again!")
                noteLine.config(fg= "red")
        else:
            Note.set("※Your Account or Password "
                     "\nis wrong! Please try again!")
            noteLine.config(fg="red")
    win = Tk()
    win.geometry("300x100+550+300")
    win.resizable(width=False, height=False)
    win.wm_title("Login")
    titleAccount = Label(win, text="Account：", font=("Arial", 10))
    titleAccount.place(x=19, y=10)
    titlePassword = Label(win, text="Password：", font=("Arial", 10))
    titlePassword.place(x=10, y=40)

    Note = StringVar()
    Note.set("※Hello!Welcome to login!")
    noteLine = Label(win,textvariable=Note, font=("Arial", 10))
    noteLine.place(x=20, y=62)

    length = 28
    textAccount = Entry(win, width=length)
    textAccount.place(x=85, y=12)
    textPassword = Entry(win, width=length,show='*')
    textPassword.place(x=85, y=42)
    LoginButton = Button(win, text="Login",font=("Arial", 10),bg="gray",command=command)
    LoginButton.place(x=242,y=65)
    def closing():
        exit()
    win.protocol("WM_DELETE_WINDOW", closing)
    win.mainloop()

#Login()