from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Radio Button")
root.iconbitmap('images/icon.ico')

# It's a little different to create radio buttons.
# 1. we put variable name as an attribute. A group of radio buttons can have the same variable name.
# 2. we assign different values to each radio button.
# 3. the variable name need to be defined presivously using Tkinter's variable function,
#    Here, we use r = IntVar(), means r is an integer.
#    correspondingly, the value for each radio button need to be a integer.
# 4. use .pack() together with creating a radio button.

# r = IntVar()
# r.set(2)  # set the default selection amount a group of radio buttons

# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()
# Radiobutton(root, text="Option 3", variable=r, value=3, command=lambda: clicked(r.get())).pack()

# myLabel = Label(root, text=r.get())  # .get() can get the value of the selected radio button.
# myLabel.pack()



# Below is the way of creating and display radia buttons using a for loop.

# This list consists several tuples, in which have two strings.
# In each tuple, the first string represents the text of a radio button,
# the second string represents the value of a radio button.
TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
    ]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()