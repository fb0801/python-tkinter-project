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



btn_1 = Button(root, text="+", padx=40,pady=20, command=button_add)
btn_2 = Button(root, text="-", padx=40,pady=20, command=button_subtract)
btn_3 = Button(root, text="/", padx=40,pady=20, command=button_divide)
btn_4 = Button(root, text="X", padx=40,pady=20, command=button_multiply)

mybtn = Button(root, text="enter your number", command =myClick)




root.mainloop()
