"""
Use the previous created image viewer application 
to show how to create the status bar
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Simple Image Viewer")
root.iconbitmap('images/icon.ico')

# Create 5 image objects using 'ImageTK' and 'Image' module from 'PIL' library.
my_img1 = ImageTk.PhotoImage(Image.open("images/1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/5.jpg"))

# Put the image objects in a list for indexing.
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# Create a label to hole the status informtion.
# 'anchor' is to display the directional text. 'E' means right.
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

# Create a 'Label' widget to hold the images,
# will show first image when app starts.
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_num):
    """function to respond clicking on >>(forward) button.

    Args:
        image_num ([int]): [the index of the images from the 'image_list']
    """
    global my_label
    global button_forward
    global button_back

    # To display new image, it's better to get rid of the old one, to avoid
    # images stacking onto each other, for saving memory and better displaying.
    my_label.grid_forget()

    # Then recreate the Label widget for new image.
    my_label = Label(image=image_list[image_num])

    # Update the image index for 'forward' and 'back' button for
    # correctly responding to the next click.
    button_forward = Button(root, text=">>", command=lambda: forward(image_num + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_num - 1))

    # In order to loop over images between clicks, we reset the image index
    # to make sure, when it reaches the last image,
    # the next forward button click will get the first image again.
    if image_num == 4:
        image_num = -1

    # Finally, put every updated widget on the screen.
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Add controls to make sure the correct information display on status bar,
    # when comes to the first or the last image.
    if image_num == -1:
        status = Label(root, text="Image " + str(image_num+len(image_list)+1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    else:
        status = Label(root, text="Image " + str(image_num+1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def back(image_num):
    """function to respond clicking on << (back) button.

    Args:
        image_num ([int]): [the index of the images from the 'image_list']
    """
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_num])
    button_forward = Button(root, text=">>", command=lambda: forward(image_num + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_num - 1))

    # In order to loop over images between clicks, we reset the image index
    # to make sure, when it reaches the first image,
    # the next back button click will get the last image again.
    if image_num == -5:
        image_num = 0

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # Add controls to make sure the correct information display on status bar,
    # when comes to the first or the last image.
    if image_num == 0:
        status = Label(root, text="Image " + str(image_num+1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    else:
        status = Label(root, text="Image " + str(image_num+len(image_list)+1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
        status.grid(row=2, column=0, columnspan=3, sticky=W+E)


# Give the correct image index for the initial function call.
button_forward = Button(root, text=">>", command=lambda: forward(1))
button_back = Button(root, text="<<", command=lambda: back(-1))
button_exit = Button(root, text="Exit Program", command=root.quit)

button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=2, pady=10)
button_exit.grid(row=1, column=1)

# 'sticky' is to stretch the status bar to the screen.
# 'W+E' meansstretch from West (left) to East (right).
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
