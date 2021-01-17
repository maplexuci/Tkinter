from tkinter import *

root = Tk()
root.title("Simple Calculator")

# 'justify' allows you input from different position. 
e = Entry(root, width=35, bg="white", borderwidth=5, justify=RIGHT)
e.insert(END, "0")
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

bg_num = 0
add_bg_num = 0
sub_bg_num = 0
mul_bg_num = 0
div_bg_num = 0

# These tags are used to moniter if buttonSubtract(),
# or buttonMultiply(), or buttonDivide() is called for the first time.
sub_init = "OFF" 
mul_init = "OFF"
div_init = "OFF"


add_active = "OFF"
sub_active = "OFF"
mul_active = "OFF"
div_active = "OFF"


def buttonNum(number):
    """Response to clicking number button."""
    
#   global variable bg_num watches for if the buttonAdd()... function is called, 
#   which means the '+'... button is clicked.
    global bg_num
    
#     when bg_num == True, the buttonAdd() or ... was called then, 
#     then the current numbers need to be cleaned for the second number to be input
    if e.get() == '0' or bool(bg_num) == True:
        bg_num = 0
        e.delete(0, END)
        
    e.insert(END, number)


def buttonClear():
    """Response to clicking Clear button."""
#   We need to declare bg_num as global varible again, because we are assinging a value to it
#   in the last line of this function.
    global bg_num
    global add_bg_num
    global sub_bg_num
    global sub_init
    global mul_init
    global div_init
    global mul_bg_num
    global div_bg_num
    global add_active
    global sub_active
    global mul_active
    global div_active

    e.delete(0, END)
    
    bg_num = 0
    add_bg_num = 0
    sub_bg_num = 0
    mul_bg_num = 0
    div_bg_num = 0

    sub_init = "OFF"
    mul_init = "OFF"
    div_init = "OFF"

    add_active = "OFF"
    sub_active = "OFF"
    mul_active = "OFF"
    div_active = "OFF"

    e.insert(END, "0")


def buttonAdd():
    """Response to clicking '+' button."""
    global add_bg_num
    global bg_num
    global math

    math = "addition"

    buttonEqual()
    operand_1 = e.get()
#     Two global variables, bg_num is used with buttonNum() function,
#     add_bg_num, which receives the value from bg_num is used for calculation.
#     because the value of variable bg_num need to be reset to 0,
#     in order to be able to insert concecutive numbers in the input box.


    bg_num = int(operand_1)
    add_bg_num = bg_num

def buttonSubtract():
    """Response to clicking '-' button."""
    global sub_bg_num
    global bg_num
    global math

    math = "subtraction"

    buttonEqual()

    operand_1 = e.get()

    bg_num = int(operand_1)
    sub_bg_num = bg_num


def buttonMultiply():
    """Response to clicking '*' button."""
    global mul_bg_num
    global bg_num
    global math

    math = "multiplication"

    buttonEqual()
    operand_1 = e.get()

    bg_num = int(operand_1)
    mul_bg_num = bg_num


def buttonDivide():
    """Response to clicking '/' button."""
    global div_bg_num
    global bg_num
    global math

    math = "division"

    buttonEqual()
    operand_1 = e.get()

    bg_num = float(operand_1)
    div_bg_num = bg_num


def buttonEqual():
    """Response to clicking '=' button."""
#   We need to declare bg_num as global varible again, 
#   because we are assigning a value to it in the last line of this function.
    global bg_num
    global sub_init
    global mul_init
    global div_init
    global add_active
    global sub_active
    global mul_active
    global div_active

#   Get the number in the input box first.
    operand_2 = e.get()

#   Then clear the input box, for output the calculation result.
    e.delete(0, END)

#   Final calculation and put it in the input box.
#   We don't need to declare add_bg_num as global variable again, 
#   because we are referencing it, but not assigning new values to it.
    if math == "addition":
        add_active = "ON"
        if sub_active == "ON":
            if sub_init == "OFF":
                e.insert(0, int(operand_2) - sub_bg_num)
                sub_init = "ON"
            else:
                e.insert(0, sub_bg_num - int(operand_2))
            sub_active = "OFF"

        if mul_active == "ON":
            if mul_init == "OFF":
                e.insert(0, int(operand_2))
                mul_init = "ON"
            else:
                e.insert(0, mul_bg_num * int(operand_2))
            mul_active = "OFF"

        if div_active == "ON":
            if div_init == "OFF":
                e.insert(0, int(operand_2))
                div_init = "ON"
            if int(operand_2) == 0:
                e.insert(0, "Error")
            else:
                e.insert(0, div_bg_num / int(operand_2))
            div_active = "OFF"
        else:
            e.insert(0, add_bg_num + int(operand_2))
#   Let bg_num have value again in order to delete the content in the input box
#   when clicking a number button again.
        bg_num = e.get()

    if math == "subtraction":
        sub_active = "ON"
        if add_active == "ON":
            e.insert(0, add_bg_num + int(operand_2))
            add_active = "OFF"

        if mul_active == "ON":
            if mul_init == "OFF":
                e.insert(0, int(operand_2))
                mul_init = "ON"
            else:
                e.insert(0, mul_bg_num * int(operand_2))
            mul_active = "OFF"

        if div_active == "ON":
            if div_init == "OFF":
                e.insert(0, int(operand_2))
                div_init = "ON"
            if int(operand_2) == 0:
                e.insert(0, "Error")
            else:
                e.insert(0, div_bg_num / int(operand_2))
            div_active = "OFF"

        else:
            if sub_init == "OFF": # Indicating the buttonSubtract() function is called for the first time.
                e.insert(0, int(operand_2) - sub_bg_num) # Value of 'sub_bg_num' is 0 in the beginning, so switch the operands to make the calculation and display correct.
                sub_init = "ON" # Then set 'sub_init' tag to be "ON", to make sure the 'else' statement is always excuted, until the buttonClear() is called.
            else:
                e.insert(0, sub_bg_num - int(operand_2))
        bg_num = e.get()

    if math == "multiplication":
        mul_active = "ON"
        if add_active == "ON":
            e.insert(0, add_bg_num + int(operand_2))
            add_active = "OFF"

        if sub_active == "ON":
            if sub_init == "OFF":
                e.insert(0, int(operand_2) - sub_bg_num)
                sub_init = "ON"
            else:
                e.insert(0, sub_bg_num - int(operand_2))
            sub_active = "OFF"

        if div_active == "ON":
            if div_init == "OFF":
                e.insert(0, int(operand_2))
                div_init = "ON"
            if int(operand_2) == 0:
                e.insert(0, "Error")
            else:
                e.insert(0, div_bg_num / int(operand_2))
            div_active = "OFF"

        else:
            if mul_init == "OFF":
                e.insert(0, int(operand_2))
                mul_init = "ON"
            else:
                e.insert(0, mul_bg_num * int(operand_2))
        bg_num = e.get()

    if math == "division":
        div_active = "ON"
        if add_active == "ON":
            e.insert(0, add_bg_num + int(operand_2))
            add_active = "OFF"

        if sub_active == "ON":
            if sub_init == "OFF":
                e.insert(0, int(operand_2) - sub_bg_num)
                sub_init = "ON"
            else:
                e.insert(0, sub_bg_num - int(operand_2))
            sub_active = "OFF"

        if mul_active == "ON":
            if mul_init == "OFF":
                e.insert(0, int(operand_2))
                mul_init = "ON"
            else:
                e.insert(0, mul_bg_num * int(operand_2))
            mul_active = "OFF"

        else:
            if div_init == "OFF":
                e.insert(0, float(operand_2))
                div_init = "ON"
            else:
                if float(operand_2) == 0:
                    e.insert(0, "Error")
                else:
                    e.insert(0, div_bg_num / float(operand_2))
        bg_num = e.get()


#  Create the buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonNum(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonNum(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonNum(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonNum(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonNum(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonNum(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonNum(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonNum(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonNum(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonNum(0))
button_add = Button(root, text="+", padx=39, pady=20, command=buttonAdd)
button_subtract = Button(root, text="-", padx=41, pady=20, command=buttonSubtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=buttonMultiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=buttonDivide)
button_equal = Button(root, text="=", padx=91, pady=20, command=buttonEqual)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=buttonClear)

# Put the buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

root.mainloop()
