from tkinter import *

root =Tk()
root.title('Calculator')


e = Entry(root, width=35, borderwidth=5)
e.grid(row=0,column=0, columnspan=3, padx=10, pady=10)

def button_add():
    return


def button_subtract():
    return

def button_divide():
    return

def button_multiply():
    return

#define btns

btn_1 = Button(root, text="1", padx=40,pady=20, command=button_add)
btn_2 = Button(root, text="2", padx=40,pady=20, command=button_add)
btn_3 = Button(root, text="3", padx=40,pady=20, command=button_add)
btn_4 = Button(root, text="4", padx=40,pady=20, command=button_add)
btn_5 = Button(root, text="5", padx=40,pady=20, command=button_add)
btn_6 = Button(root, text="6", padx=40,pady=20, command=button_add)
btn_7 = Button(root, text="7", padx=40,pady=20, command=button_add)
btn_8 = Button(root, text="8", padx=40,pady=20, command=button_add)
btn_9 = Button(root, text="9", padx=40,pady=20, command=button_add)
btn_0 = Button(root, text="0", padx=40,pady=20, command=button_add)


btn_add = Button(root, text="+", padx=40,pady=20, command=button_add)
btn_sub = Button(root, text="-", padx=40,pady=20, command=button_subtract)
btn_div = Button(root, text="/", padx=40,pady=20, command=button_divide)
btn_mul = Button(root, text="X", padx=40,pady=20, command=button_multiply)

mybtn = Button(root, text="enter your number", command =myClick)


#put btns on screeen
btn_1.grid()
btn_2.grid()
btn_3.grid()
btn_4.grid()
btn_5.grid()
btn_6.grid()
btn_7.grid()
btn_8.grid()
btn_9.grid()
btn_0.grid()
btn_add.grid()
btn_sub.grid()
btn_div.grid()
btn_mul.grid()


root.mainloop()
