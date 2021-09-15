from tkinter import *

root = Tk()
root.title('learn to code')
root.iconbitmap()

button_quit =Button(root, text="Exit program", command=root.quit)
button_quit.pack()

root.mainloop()
