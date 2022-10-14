from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Check")
root.geometry("400x400")


def show():
    myLabel["text"]=var.get()


var = StringVar()

c = Checkbutton(root, text="Check this box, I dare you!", command=show, variable = var, onvalue="Pizza", offvalue="hamburger")
c.deselect()
c.pack()


myLabel = Label(root, text=var.get())
myLabel.pack()

#myButton = Button(root, text= "Show Selection", command = show)
#myButton.pack()



root.mainloop()
