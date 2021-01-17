from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Add Frame")
root.iconbitmap('images/icon.ico')

# You need to put something in the frame to display the frame.
# the padx and pady in the frame is for the elements inside of the frame, that relative to frame.
# the padx and pady in frame.pack() are for the frame, that relative to root.
# A frame doesn't have to have the text. So the 'text' attribute can be removed.
frame = LabelFrame(root, text="This is the first frame...", padx=100, pady=30)
frame.pack(padx=10, pady=10)

# Display the button in frame, not in the root window.
button1 = Button(frame, text="Click here")
button2 = Button(frame, text="Click here as well")

# Inside of the fram, you can use grid() to display widget inside of the frame.
button1.grid(row=0, column=0)
button2.grid(row=1, column=1)

# You can use .pack() as well.
# button1.pack()
# button2.pack()


root.mainloop()