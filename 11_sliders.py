from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Sliders")
root.iconbitmap('images/icon.ico')
root.geometry("400x400")

vertical = Scale(root, from_=0, to=400)
vertical.pack() # For this, you need to .pack() in a seprately.

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()


def slide():
    my_label = Label(root, text=horizontal.get()).pack()

    # Change window size based on the slider value
    root.geometry(str(horizontal.get()) + "x400")

my_btn = Button(root, text="Get slider value", command=slide).pack()


root.mainloop()
