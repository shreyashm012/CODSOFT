from tkinter import *
root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    borderwidth=15

def button_clear():
    borderwidth=5
    e.delete(0, END)
    borderwidth=15

def button_add():
    borderwidth=15
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    borderwidth=5
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))

def button_subtract():
    borderwidth=5
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    borderwidth=5
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    borderwidth=5
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

b1 = Button(root, text="1", padx=40, pady=20,fg='yellow',bg='black', command=lambda: button_click(1))
b2 = Button(root, text="2", padx=40, pady=20,fg='yellow',bg='black', command=lambda: button_click(2))
b3 = Button(root, text="3", padx=40, pady=20,fg='yellow',bg='black', command=lambda: button_click(3))
b4 = Button(root, text="4", padx=40, pady=20,fg='yellow',bg='black', command=lambda: button_click(4))
b5 = Button(root, text="5", padx=40, pady=20,fg='yellow',bg='black', command=lambda: button_click(5))
b6 = Button(root, text="6", padx=40, pady=20,fg='yellow',bg='black', command=lambda: button_click(6))
b7 = Button(root, text="7", padx=40, pady=20,fg='yellow',bg='black', command=lambda: button_click(7))
b8 = Button(root, text="8", padx=40, pady=20,fg='yellow',bg='black', command=lambda: button_click(8))
b9 = Button(root, text="9", padx=40, pady=20,fg='yellow',bg='black', command=lambda: button_click(9))
b0 = Button(root, text="0", padx=40, pady=20,fg='yellow',bg='black', command=lambda: button_click(0))


button_add = Button(root, text="+",fg="white",bg="black", padx=39, pady=20, command=button_add)
button_equal = Button(root, text="=",fg="red",bg="black", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear",fg="red",bg="black", padx=79, pady=20, command=button_clear)

button_subtract = Button(root, text="-",fg="white",bg="black", padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text="*",fg="white",bg="black", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/",fg="white",bg="black", padx=41, pady=20, command=button_divide)


b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)

b0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)
root.mainloop()

