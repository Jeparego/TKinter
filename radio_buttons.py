from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Radio Buttons')

r = IntVar()

def clicked(value):
    myLabel["text"]= value

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Oion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text = text, variable=pizza, value=mode).pack(anchor=W)
    
##Radiobutton(root, text= "Option 1", variable = r, value =1, command= lambda: clicked(r.get())).pack()
##Radiobutton(root, text= "Option 2", variable = r, value =2, command= lambda: clicked(r.get())).pack()
##
myLabel = Label(root, text=pizza.get())
myLabel.pack()

myButton = Button(root, text="Click me!", command = lambda: clicked(pizza.get())).pack()


root.mainloop()
