from tkinter import *

class GUI(Tk):
     def __init__(self):
          super().__init__()
          self.geometry("400x500")
     def status(self):
          self.var= StringVar()
          self.var.set("ready")
          self.statusbar=Label(self,textvar=self.var,relief=SUNKEN ,anchor="w")
          self.statusbar.pack(side=BOTTOM,fill=X)
     def click(self):
          print("cloicked")
     def createbotton(self,inptext):
          Button(text=inptext,command=self.click).pack()
if __name__=='__main__':
     mad=GUI()
     mad.status()
     mad.createbotton("nadhu")
     mad.mainloop()






