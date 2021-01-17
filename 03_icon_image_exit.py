from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Add icon and images")
root.iconbitmap('images/icon.ico')

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

my_img = ImageTk.PhotoImage(Image.open("images/example_img.png"))
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()
