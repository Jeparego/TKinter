from tkinter import *



root = Tk()
root.title("Claculator")
    e = Entry(root, width=45, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

f_num="0"
b_n=0

def button_click(number):
    global b_n
    if b_n == 1:
        e.delete(0, END)
        e.insert(0, number)
        b_n=0
    else:
        current=e.get()
        e.delete(0, END)
        e.insert(0, str(current)+str(number))

def button_clear():
    global b_n
    global f_m
    b_n = 0
    f_m ="0"
    e.delete(0,END)
    

def button_add():
    global f_num
    if (f_num =="0"):
        f_num = int(e.get())
        e.delete(0, END)
    else:
        n_num= int(e.get())
        e.delete(0,END)
        f_num+= n_num
        e.insert(0, f_num)
        global b_n
        b_n=1
        

    
        
            
def button_equal():
    global f_num
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num +int(second_number))
    f_num ="0"
        
    


button_1 = Button(root, text="1", padx = 40, pady=20, command=lambda: button_click(1)).grid(row=3, column=0)
button_2 = Button(root, text="2", padx = 40, pady=20, command=lambda: button_click(2)).grid(row=3, column=1)
button_3 = Button(root, text="3", padx = 40, pady=20, command=lambda: button_click(3)).grid(row=3, column=2)   
button_4 = Button(root, text="4", padx = 40, pady=20, command=lambda: button_click(4)).grid(row=2, column=0)
button_5 = Button(root, text="5", padx = 40, pady=20, command=lambda: button_click(5)).grid(row=2, column=1)
button_6 = Button(root, text="6", padx = 40, pady=20, command=lambda: button_click(6)).grid(row=2, column=2)
button_7 = Button(root, text="7", padx = 40, pady=20, command=lambda: button_click(7)).grid(row=1, column=0)
button_8 = Button(root, text="8", padx = 40, pady=20, command=lambda: button_click(8)).grid(row=1, column=1)
button_9 = Button(root, text="9", padx = 40, pady=20, command=lambda: button_click(9)).grid(row=1, column=2)
button_0 = Button(root, text="0", padx = 40, pady=20, command=lambda: button_click(0)).grid(row=4, column=0)
button_clear = Button(root, text="CLEAR", padx = 75, pady=20, command= button_clear).grid(row=4, column=1, columnspan=2)
button_add = Button(root, text="+", padx = 40, pady=20, command=button_add).grid(row=5, column=0)
button_equal = Button(root, text="=", padx = 80, pady=20, command= button_equal).grid(row=5, column=1, columnspan=2)


#myLabel1 = Label(root, text="Hola Mundo").grid(row=0, column=0)
#myLabel2 = Label(root, text="Hola Universo").grid(row=1, column=1)
myButton = Button(root, text="Enter Your Name", padx=20)


    
root.mainloop()


