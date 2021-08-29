from tkinter import *
import tkinter.messagebox as tmsg

root= Tk()
root.title("madhikar")
root.geometry("500x600")

def myfunc():
     print("madhukar you did it")
 
def help():
     print("its help")
     tmsg.showinfo("help","we will help you")

def rate():
     # tmsg.showinfo("rate", "rate  us with your experience")
     value= tmsg.askquestion("rate","have you enjoyed our GUI")
     print(value)
mainmenu=Menu(root)
menu1= Menu(mainmenu, tearoff=0)

menu1.add_command(label="create new file",command=myfunc)
menu1.add_command(label="open file",command=myfunc)
menu1.add_command(label="Help",command=help)
menu1.add_command(label="contact us",command=myfunc)
menu1.add_command(label="Rate Us",command=rate)
menu1.add_command(label="exit",command=quit)

root.config(menu=mainmenu)
mainmenu.add_cascade(label="file", menu=menu1)

slider= Scale(root, from_=0 ,to= 100, tickinterval=25)
slider.set(50)
slider.pack()
slider2= Scale(root, from_=0 ,to= 100, orient= HORIZONTAL)
slider2.pack()

root.mainloop()