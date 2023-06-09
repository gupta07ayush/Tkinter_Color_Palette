# Python Program to create color chooser dialog box

# importing tkinter module
from tkinter import *

# importing the choosecolor package
from tkinter import colorchooser

# function that will be invoked when the button will be clicked in the main window.


def choose_color():

    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title="Choose your favorite color")
    print(color_code)
    for i in color_code:
        print(i)


root = Tk()
root.title('Tkinter Color Palette')
root.geometry("500x500")

select_color_button = Button(root, text='Select color', command=choose_color)
select_color_button.pack()

# start the GUI loop
root.mainloop()
