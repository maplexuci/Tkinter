from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Create New Window")
root.iconbitmap('images/icon.ico')


def show():
        """"""
        root.update()
        root.deiconify()


def on_closing():
    top.destroy()
    show()


def onClosing(otherWindow):
        """"""
        otherWindow.destroy()
        show()

def openNew():
    global my_img
    global top
    # We need to make this variable as global, 
    # you could understand it like this: the button which calls the function is in the root window,
    # my_img is a local variable, when you need to load image in the second window,
    # python thinks this local variable as garbage, and go through its garbage collection mechanism.
    # Therefore, making it as global letting the new window is able to access this variable. 
    # However, local variable works in the root window.
    root.withdraw()
    top = Toplevel()
    top.title("Second Window")
    lbl = Label(top, text="This is the second window").pack()
    my_img = ImageTk.PhotoImage(Image.open("images/1.jpg"))
    img_lbl = Label(top, image=my_img).pack()
    handler = lambda: onClosing(top)
    btn2 = Button(top, text="close window", command=handler).pack()

    top.protocol("WM_DELETE_WINDOW", on_closing)


button = Button(root, text="Oen the second window", command=openNew).pack()

root.mainloop()
