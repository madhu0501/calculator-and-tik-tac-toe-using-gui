from tkinter import *
root=Tk()
root.geometry("300x400")
def getvalues():
     print(uservalue.get())
     print(passvalue.get())

user=Label(root, text="username")
password=Label(root,text="password")
user.grid(row=0,column=0)
password.grid(row=1,column=0)

uservalue=StringVar()
passvalue= StringVar()

userentry = Entry(root, textvariable=uservalue)
userentry.grid(row=0,column=1)
passentry= Entry(root, textvariable=passvalue)
passentry.grid(row=1,column=1)
Button(text="submit",command=getvalues).grid(row=3,column=0)

root.mainloop()
