from tkinter import *

root =Tk()
root.title('Calculator')


e = Entry(root, width=35, borderwidth=5)
e.grid(row=0,column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    #e.delete(0,END) #delete what alredy there
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number)) #add it to the box

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0,END)


def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_number)
    e.delete(0,END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = 'muliplication'
    f_num = int(first_number)
    e.delete(0,END)

def button_equal():
    
    second_number = e.get()
    e.delete(0,END)
    if math =="addition":
        e.insert(0, f_num + int(second_number))
        
    if math =="subtraction":
        e.insert(0, f_num - int(second_number))
        
    if math =="muliplication":
        e.insert(0, f_num * int(second_number))
        
    if math =="division":
        e.insert(0, f_num / int(second_number))

#define btns

btn_1 = Button(root, text="1", padx=40,pady=20, command=lambda: button_click(1))
btn_2 = Button(root, text="2", padx=40,pady=20, command=lambda: button_click(2))
btn_3 = Button(root, text="3", padx=40,pady=20, command=lambda: button_click(3))
btn_4 = Button(root, text="4", padx=40,pady=20, command=lambda: button_click(4))
btn_5 = Button(root, text="5", padx=40,pady=20, command=lambda: button_click(5))
btn_6 = Button(root, text="6", padx=40,pady=20, command=lambda: button_click(6))
btn_7 = Button(root, text="7", padx=40,pady=20, command=lambda: button_click(7))
btn_8 = Button(root, text="8", padx=40,pady=20, command=lambda: button_click(8))
btn_9 = Button(root, text="9", padx=40,pady=20, command=lambda: button_click(9))
btn_0 = Button(root, text="0", padx=40,pady=20, command=lambda: button_click(0))



btn_add = Button(root, text="+", padx=40,pady=20, command=button_add)
btn_sub = Button(root, text="-", padx=40,pady=20, command=button_subtract)
btn_div = Button(root, text="/", padx=40,pady=20, command=button_divide)
btn_mul = Button(root, text="X", padx=40,pady=20, command=button_multiply)
btn_clr = Button(root, text="CE", padx=90,pady=20, command=button_clear)
btn_eql = Button(root, text="=", padx=91,pady=20, command=button_equal)
btn_dot = Button(root, text='.', padx=40, pady=20, command=button_add)



#put btns on the screeen
btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_0.grid(row=4, column=0)



btn_add.grid(row=4, column=3)
btn_sub.grid(row=2, column=3)
btn_div.grid(row=3, column=3)
btn_mul.grid(row=1, column=3)
btn_clr.grid(row=5, column=0, columnspan =2)
btn_eql.grid(row=5, column=2, columnspan =2)
btn_dot.grid(row=4, column=2)

root.mainloop()
