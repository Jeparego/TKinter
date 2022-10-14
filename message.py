from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title("Message Box")

#(ok):showinfo, showwarning, showerror, (yes, no): askquestion, (1,0):askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is my Popup!", "Hello World")
##    Label(root, text=response).pack()
    if response ==1:
        Label(root, text="Yes").pack()
    else:
        Label(root, text="No").pack()
        

Button(root, text = "Popup", command =popup).pack()


root.mainloop()
