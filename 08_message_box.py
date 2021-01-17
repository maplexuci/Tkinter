from tkinter import *
from PIL import ImageTk, Image

# Remember to import messagebox modual from tkinter.
from tkinter import messagebox

root = Tk()
root.title("Message Box")
root.iconbitmap('images/icon.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
# are the methods of the messagebox and can be used for display different
# types of popup window, some of them are even comes with sound.


def popup():
    # messagebox.showinfor() function have two parameters,
    # the first one is the popup window title.
    # the second one is the message you want to show in the popup window.
    # The response to the popup windows returns different value based on the window type.
    # for example, askyesno() methods, in the meassage box, if you click 'Yes' button,
    # it returns a integer 1, 'No' returns integer 0.
    # But in .askquestion() method, 'Yes' returns string 'yes', and 'No' returns 'no'.
    response = messagebox.askyesno("This is my Popup", "This is a warning")

    # Create a label to display the return value of the response to each message box.
    Label(root, text=response).pack()

    # Then we can do different thing based on the choices we made.
    if response == 1:
        Label(root, text="You Clicked Yes!").pack()
    else:
        Label(root, text="You Clicked No!").pack()


Button(root, text="Popup", command=popup).pack()


root.mainloop()
