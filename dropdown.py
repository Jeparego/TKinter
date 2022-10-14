from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Check")
root.geometry("400x400")

def show(string):
    myLabel["text"]= clicked.get()
    print(clicked.get())



weekdays= [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
]

clicked= StringVar()

drop = OptionMenu(root, clicked, *weekdays , command=show)
drop.pack()

myLabel = Label(root, text=clicked.get())
myLabel.pack()
if clicked.get()== '':
    print("OK")


root.mainloop()
