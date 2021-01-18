from tkinter import *
from PIL import ImageTk, Image

# You need to import the filedialog modual of tkinter
from tkinter import filedialog

root = Tk()
root.title("Create New Window")
root.iconbitmap('images/icon.ico')

# root.filename = filedialog.askopenfilename(initialdir="/images", title="Select A File", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("All files", "*.*")))

# # This label can be used to receive the path and name of the selected file.
# my_label = Label(root, text=root.filename).pack()

# # This can open the file you selected in the label widget of the root window
# my_image = ImageTk.PhotoImage(Image.open(root.filename))
# my_image_label = Label(image=my_image)
# my_image_label.pack()


def openFile():
    global my_image

    # This function returns the location of the selected file you want to open,
    # once you have the location, you can open it using certain methods for different file types.
    root.filename = filedialog.askopenfilename(initialdir="/images", title="Select A File", filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"), ("All files", "*.*")))

    # From here, you can see 'root.filename' is the path of the selected file.
    my_label = Label(root, text=root.filename).pack()

    # This can open the file you selected in the label widget of the root window.
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image)
    my_image_label.pack()


my_btn = Button(root, text="Open FIle", command=openFile).pack()

root.mainloop()
