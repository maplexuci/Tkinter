from tkinter import *

root = Tk()
root.title("Dropdown menu")
root.iconbitmap('images/icon.ico')
root.geometry("400x400")


def show():
    myLable = Label(root, text=var.get()).pack()


options = [ "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday"
    ]

var = StringVar()
var.set(option[0])

# Note that you need the '*' with the 'options'
drop = OptionMenu(root, var, *options)
drop.pack()

myButton = Button(root, text="Show selection", command=show).pack()

root.mainloop()
