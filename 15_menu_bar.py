from tkinter import *

root = Tk()
root.title("Menu Bar")
root.iconbitmap('images/icon.ico')
root.geometry("400x400")


my_menu = Menu(root)
root.config(menu=my_menu)

# Command
def our_command():
    pass


# Create File menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=our_command)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Create Edit menu
edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=our_command)
edit_menu.add_command(label="copy", command=our_command)


root.mainloop()
