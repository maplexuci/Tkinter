from tkinter import *

root = Tk()
root.title("Image and Round Button")
root.iconbitmap('images/icon.ico')
root.geometry("400x400")


def thing():
    my_label.config(text="You clicked the button")

img_button = PhotoImage(file='images/img_button.png')
my_button = Button(root, image=img_button, borderwidth=0, command=thing)
my_button.pack(pady=20)

my_label = Label(root, text='')
my_label.pack(pady=20)


root.mainloop()
