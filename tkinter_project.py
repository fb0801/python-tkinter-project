from tkinter import *

root =Tk()
root.title('Calculator')


e = Entry(root, width=35, borderwidth=5)
e.grid(row=0,column=0, columnspan=3, padx=10, pady=10)

e.insert(0, "Enter your number")

def myClick():
    hello = "hello" + e.get()
    

    #creating lbl widget
    myLabel = Label(root, text="Hello word!")
    myLabel.pack()

mybtn = Button(root, text="enter your number", command =myClick)




root.mainloop()
