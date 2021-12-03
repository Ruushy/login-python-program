from tkinter import *
from tkinter import messagebox

def info():
    username = user.get()
    password = pin.get()
    username = username.lower()
    if username == "" and password == "":
        messagebox.showinfo( " " ," blink is not allowed ")
    elif username == "ruushy" and password == "1234":
        messagebox.showinfo(" " ,"login succsucfully ")
    else :
        messagebox.showinfo("" ," password or username is incorrect ")
root = Tk()
root.geometry("500x500")


entry1 = Label(root , text="username" )
entry1.place(x= 20 , y = 40)
entry2 = Label(root , text="password" )
entry2.place(x= 20 , y = 100)
user = Entry()
user.place( x = 100 , y = 40 , width = 200)
pin = Entry()
pin.place( x = 100 , y = 100 , width = 200  )
button = Button(root , text = "submit" , width = 20 , command = info)
button.place(x = 140 , y = 140)
root.mainloop()
