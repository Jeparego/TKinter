from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Image Carrusel")
root.iconbitmap("")

my_img1 = ImageTk.PhotoImage(Image.open("images/1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/5.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]


status = Label(root, anchor= E, relief=SUNKEN, bd=4, text = "Image 1 of " + str(len(image_list)))
status.grid(row=2, column =0, columnspan=3, sticky = W+E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back
##    my_label.grid_forget()
##    my_label = Label(image = image_list[image_number-1])
##    my_label.grid(row=0, column=0, columnspan=3)
    my_label["image"] = image_list[image_number-1]
    button_forward["command"]= lambda: forward(image_number +1)
    button_back["command"]= lambda: back(image_number-1)
    button_back["state"]= ACTIVE
    if image_number == len(image_list):
        button_forward["state"]= DISABLED
    status["text"] = "Image " + str(image_number) + " of"  + str(len(image_list))
        
    
                        

def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label["image"] = image_list[image_number-1]
    button_forward["command"]= lambda: forward(image_number +1)
    button_back["command"]= lambda: back(image_number-1)
    button_forward["state"]= ACTIVE
    if image_number==1:
        button_back["state"]= DISABLED
    status["text"] = "Image " + str(image_number) + " of" + str(len(image_list))




button_back = Button(root, text="<<", command=back, state= DISABLED)
button_forward = Button(root, text=">>", command = lambda: forward(2))

button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2)

button_exit = Button(root, text= "Exit program", command=root.quit)
button_exit.grid(row=1, column=1, pady=10)

status.grid(row=2, column =0, columnspan=3, sticky = W+E)

root.mainloop()
