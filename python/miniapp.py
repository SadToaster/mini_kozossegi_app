
from tkinter import *
from random import *
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import ttk

# Color palette: #00ABC3, #3C4048, #B2B2B2, #EAEAEA

root = Tk()
root.title("Mini közösségi app")
root.config(bg="#00ABC3")
root.geometry('500x500')
Titlefont = tkFont.Font(family="Times New Roman", size=18, weight="bold", underline=1 )
Labelfont = tkFont.Font(family="Times New Roman", size=12, weight="bold", underline=1 )

user = ""
passw = ""

Cim = Label(root,text="Kérem adja meg a bejelentkezési adatait: ", font=Titlefont, fg="white",bg="#00ABC3") 
Cim.place(relx=0.5,rely=0.1,anchor=N)

UsernameFrame = Frame(root,bg="#000000")
UsernameFrame.place(relx=0.4,rely=0.2, anchor=N)

user = Label(UsernameFrame,text="Username:",bg="#00ABC3",font=Labelfont)
user.grid(column=0,row=2)
user_entry = Entry(UsernameFrame, textvariable = user,width=50)
user_entry.grid(column=1,row=2)

root.mainloop()