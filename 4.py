from tkinter import *
def getvalues():
     print("yaaa we did it broo")
root=Tk()
root.geometry("400x400")
Label(root,text="well come to max travels",pady=30).grid(row=0,column=2)

name=Label(root,text="name")
phone=Label(root,text="phone")
gender=Label(root,text="gender")
emergency=Label(root,text="emergency contact")
payment=Label(root,text="paymentmethod")

name.grid(row=1,column=1)
phone.grid(row=2,column=1)
gender.grid(row=3,column=1)
emergency.grid(row=4,column=1)
payment.grid(row=5,column=1)

namevalue= StringVar()
phonevalue= StringVar()
gendervalue= StringVar()
emergencyvalue= StringVar()
paymentvalue= StringVar()

nameentry=Entry(root,textvariable=namevalue).grid(row=1,column=2)
phoneentry=Entry(root, textvariable=phonevalue).grid(row=2,column=2)
genderentry=Entry(root,textvariable=gendervalue).grid(row=3,column=2)
emergencyentry=Entry(root,textvariable=emergencyvalue).grid(row=4,column=2)
paymententry=Entry(root,textvariable=paymentvalue).grid(row=5,column=2)

Button(root,text="submit",command=getvalues).grid(row=7,column=3)

root.mainloop()


