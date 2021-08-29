from tkinter import *
root=Tk()
# root.geometry('456x468')
c_width=400
c_height=500
root.geometry(f"{c_width}x{c_height}")
root.title("widget")
c_widget = Canvas(root, width = c_width,height=c_height)
c_widget.pack()
c_widget.create_line(0,0,300,500,fill="red")
c_widget.create_line(500,200,300,20,fill="red")

c_widget.create_rectangle(20,30,400,200,fill="blue")
c_widget.create_text(50,50, text="madhukar",fill="red")

def harry(event):
     print("yaa huuuu...")

mad=Button(root, text='click me here')
mad.grid(row=0,column=23)

mad.bind('<Double-1>',quit)
mad.bind('<Button->',harry)
root.mainloop()