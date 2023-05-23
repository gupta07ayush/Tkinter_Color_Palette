Python provides many options for Graphical user interface development. Tkinter is the most commonly used option apart from all other available alternatives.

### The steps involved in developing a basic tkinter app are:

1. Importing the Tkinter module
2. Creating the main window.
3. Insert as many as widgets as you want to the main window.
4. Apply the event trigger on all the widgets

# Creating choose color dialogue box using Tkinter

Tkinter module has a package in it named colorchooser. This package helps in developing the color chooser dialogue box.
This package has a function named askcolor() that plays a major role.

## askcolor()

This function belongs to the colorchooser package of tkinter module. The function helps in creating a color chooser dialog box. As soon as the function is called, it makes the color chooser dialogue box pop up. The function returns the hexadecimal code of the color selected by the user.

`colorchooser.askcolor()`
