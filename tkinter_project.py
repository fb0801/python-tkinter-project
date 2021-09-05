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
btn_clr = Button(root, text="CE", padx=40,pady=20, command=button_multiply)
btn_eql = Button(root, text="=", padx=40,pady=20, command=button_multiply)




#put btns on the screeen
btn_1.grid(row=, column=)
btn_2.grid(row=, column=)
btn_3.grid(row=, column=)
btn_4.grid(row=, column=)
btn_5.grid(row=, column=)
btn_6.grid(row=, column=)
btn_7.grid(row=, column=)
btn_8.grid(row=, column=)
btn_9.grid(row=, column=)
btn_0.grid(row=, column=)



btn_add.grid(row=, column=)
btn_sub.grid(row=, column=)
btn_div.grid(row=, column=)
btn_mul.grid(row=, column=)
btn_clr.grid(row=, column=)
btn_eql.grid(row=, column=)


root.mainloop()
