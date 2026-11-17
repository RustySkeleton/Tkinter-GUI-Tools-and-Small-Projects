# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 19:37:18 2026

@author: RAJ
"""

# Widgets are the building blocks of tkinter
# Widgets : Text, Buttons, Checkboxes, Menus, Frames, etc.
# Understanding widgets and controlling them is the key to mastering any GUI framework
# You always place widgets in such an arrangement that you get some kind of interface

# Tkinter has two set of widgets
# tk widgets were the original ones
# ttk widgets were added later on (these are much more modern)

import tkinter as tk
from tkinter import ttk

def button_function():
    print("A button was pressed")
def hello():
    print("Hello!")
# create a window, the variable is sometimes also called root or app
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x700")

# ttk label
label = ttk.Label(master = window, text = "This is a text")
label.pack()

# tk text
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# my label
my_label = ttk.Label(master = window, text = "My Label")
my_label.pack()

# Hello button
# button2 = ttk.Button(master = window, text = "Another Button", command = hello)
button2 = ttk.Button(master = window, text = "Another Button", command = lambda : print("hello"))
button2.pack()
# the button doesn't necessarily have a pre-existing function, we can also define a lambda function in command
# ttk button
button = ttk.Button(master = window, text = "A Button", command = button_function)
button.pack()

# run 
window.mainloop() 



# What does the mainloop do?
# Updates the gui
# Checks for events(button clicks, mouse movement, closing the window)
# Any code after the mainloop statement only runs when the window is closed