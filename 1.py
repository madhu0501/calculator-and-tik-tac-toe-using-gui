from tkinter import *
# iconarchieve
root = Tk()
# root.geometry("50x400")
root.minsize(600,600)
root.title("CALCULATOR")
# creating a icon to app
# root.iconbitmap('app.ico')
    # label_1.grid(row=0,column=4)
e1=Entry(root,width=30,fg='blue')
e1.grid(row=0 , column=1)

e2=Entry(root,width=30,fg='blue')
e2.grid(row=0 , column=3)

def button1():
    label_2=Label(root,text="Well come" + ' ' + e1.get(),fg='grey')
    label_2.grid(row=3,column=1)
    e1.delete(0,END)
def button2():
    Label_2 = Label(root,text="And ur number is"+ ' '+ e2.get(),fg="red")
    Label_2.grid(row=3 , column=3)
    e2.delete(0,END)



b1= Button(root,text="Enter your name" , command=button1, fg='brown',bg='yellow' ,padx=10,pady=10)
b1.grid(row=2, column=1)

b2= Button(root,text="Enter your number" , command=button2, fg='brown',bg='yellow' ,padx=10,pady=10)

b2.grid(row=2, column=3)

root.mainloop()