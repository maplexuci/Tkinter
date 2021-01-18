from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Checkboxes")
root.iconbitmap('images/icon.ico')
root.geometry("400x400")

# Create checkboxes is somewhat similar than radio buttons.

def show():
    # This function will show the return value for check or unchecking the checkbox
    # By default, 1 for check, 0 for uncheck.
    myLabel = Label(root, text=var.get()).pack()


# Therefore, create a integer tkinter variable, representing the return value of the checkbox
# You can change the default return values for check and uncheck, if you change to a string, 
# you need to modify var = StringVar().

# By define a string variable, you automatically activated the
# 'tristatevalue' attribute, whose default value is empty string,
# no matter if you set 'onvalue' of 'offvalue' or not.
# On screen, the checkbutton in its third state looks greyed out but checked,
# you need to click it to let it become checked state.
var = StringVar()

# changs the default return value using 'onvalue' or 'offvalue', you can change it into anything.
# However, this comes with an issue that the checkbox will be in check status by default 
# and the .get() methods gets empty value.
c = Checkbutton(root, text="Check this box", variable=var, onvalue='on', offvalue="off")

# To make it uncheck by default, you can either use .deselect() method before put it on the screen.
# OR, you can set the variable of the checkbutton to any integer, i.e. 5.
# Note that, the integer set for the variable only serves as the value for the first time
# the checkbutton displays in the window. 
# Therefore, for consistency, it's better to set it to its 'offvalue', whether the default one or the changed one.

# c.deselect()  # Solution 1
var.set("off")  # Solution 2
c.pack()


myButton = Button(root, text="Show selection", command=show).pack()

root.mainloop()
