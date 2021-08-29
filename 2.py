from tkinter import *
root=Tk()
root.title("gui")
root.geometry('500x600')


# radio bottons in gui 
q=IntVar()
q.get()
q.set(2)

def click1(value):
     Label_1=Label(root, text=value)
     Label_1.pack()

Radiobutton(root, text="opt1", variable=q ,value =1).pack()
Radiobutton(root, text="opt2", variable=q ,value =2).pack()
Radiobutton(root, text="opt3", variable=q ,value =3).pack()
Radiobutton(root, text="opt4", variable=q ,value =4).pack()

mylabel= Label(root, text=q.get())
mylabel.pack()
b1= Button(root, text="submit",command= lambda:click1(q.get()))
b1.pack() 
# end of radio buttons

text1=Label(root,text="kkksld,ncjhdh;lmmmmmmmmmmmmmmmmmmmmmmmkaa,a,a,,,,,,,,,,,,,,,a,aaaaaa,a,\naaaaaaaaaaaaaammmmmmmmmmmmmmajaaaaaaau88888888888888888888yyyyyyyyyyyyyyyyyyygggggggggggggg\ngggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggiiiiiiiiiiiiiiiuiuiuijjjjjjj\n,\njjiillllllllllllllllllssssss233333333333344444444456531111111111111122222222222224444444444\n44400000000jkxahakkkj", fg="red", bg="yellow", borderwidth=5,padx=50,pady=89 )
# side= bottom,top,left ,right
text1.pack(anchor="se",fill="y", padx=28,pady=59)                   

f1=Frame(root,bg="yellow")
f1.pack( side=LEFT,fill="y")
l1=Label(f1,text="here we goooooo",font="helvetica 16 bold")
l1.pack(pady=179)


root.mainloop()