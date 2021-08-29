from tkinter import *

root=Tk()
root.title("Calculator")
# root.iconbitmap('1.ico')
# root.wm_iconbitmap("1.ico")
root.geometry("500x600")

def click(event):
     global scvalue
      
     text=event.widget.cget("text")
     if text == "=":
          if scvalue.get().isdigit():
               value=scvalue.get()
          else:
           try:
               value= eval(screen.get())
           except:
               #  print(e)
                value="Error"
          scvalue.set( value)
          screen.update()
               
     elif text == "c":
          scvalue.set("")
          screen.update()
     else:
          scvalue.set(scvalue.get() + text)
          screen.update()





scvalue = StringVar()
scvalue.set("")
screen=  Entry(root, textvar=scvalue,fg= "red" ,bg="light blue" ,font="lucida 25 bold")
screen.pack(fill=X, ipadx=20 ,padx= 15 , pady=5)

f=Frame(root , bg="grey")

b=Button(f, text="9" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT , padx=15,pady=5)
b.bind("<Button-1>",click)

b=Button(f, text="8" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT , padx=15 , pady= 5)
b.bind("<Button-1>",click)

b=Button(f, text="7" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

f.pack() 


f=Frame(root , bg="grey")

b=Button(f, text="6" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT , padx=15,pady=5)
b.bind("<Button-1>",click)

b=Button(f, text="5" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT , padx=15 , pady= 5)
b.bind("<Button-1>",click)

b=Button(f, text="4" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root , bg="grey")

b=Button(f, text="3" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT , padx=15,pady=5)
b.bind("<Button-1>",click)

b=Button(f, text="2" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT , padx=15 , pady= 5)
b.bind("<Button-1>",click)

b=Button(f, text="1" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root , bg="grey")

b=Button(f, text="0" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT , padx=16,pady=6)
b.bind("<Button-1>",click)

b=Button(f, text="-" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT , padx=16 , pady= 6)
b.bind("<Button-1>",click)

b=Button(f, text="+" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT,padx=16,pady=6)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root , bg="grey")

b=Button(f, text="/" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT , padx=16,pady=6)
b.bind("<Button-1>",click)

b=Button(f, text="c" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT , padx=15 , pady= 7)
b.bind("<Button-1>",click)

b=Button(f, text="=" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT,padx=17,pady=7)
b.bind("<Button-1>",click)

f.pack()

f=Frame(root , bg="grey")

b=Button(f, text="%" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT , padx=14,pady=4)
b.bind("<Button-1>",click)

b=Button(f, text="*" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT , padx=16 , pady= 6)
b.bind("<Button-1>",click)

b=Button(f, text="7" ,padx=5, pady=3,font="lucida 24 bold")
b.pack(side=LEFT,padx=14,pady=4)
b.bind("<Button-1>",click)

f.pack()
root.mainloop()
