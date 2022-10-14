from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Dialog")

def openfile():
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/rengi/Documents/Python/images",title="Select a file", filetypes= (("png","*.png"),("all", "*.*")))
    lbl["text"] = root.filename
    
lbl = Label(root, text="slect file")
lbl.pack()
Button(root, text="Open File", command=openfile).pack()




root.mainloop()
