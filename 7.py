from tkinter import *
root=Tk()
root.geometry("500x400")
root.title("listbox")

bar= Scrollbar(root)
bar.pack(side=RIGHT, fill=Y)

lbox=Listbox(root,bg="grey",fg="blue", yscrollcommand=bar.set)
for i in range(400):
     lbox.insert(END, f'item is ={i}')
lbox.pack(fill="both")
bar.config(command=lbox.yview)

lbox.insert(END, "first item")

def add():
     global i
     lbox.insert(ACTIVE,f'item number:{i}')
     i+=1
i=0
Button(root, text="add item",command=add).pack()


root.mainloop()