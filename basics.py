# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 18:45:23 2026

@author: RAJ
"""

import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

# window
window = ttk.Window(themename = "darkly")
window.title("Demo")
window.geometry("300x150") # window.geometry("widthxheight")

# Label is text in tkinter
# pack to add it to the widget, if owner is window, it'll be added to the window
# while packing we can define its alignment and padding

# title
title_label = ttk.Label(master = window, text = "Miles to Kilometers", font = "Calibri 24 bold") # ttk.Label(master = parent, text = "Text to be shown", font = "Font_style font_size")
title_label.pack()

# input field 
input_frame = ttk.Frame(master = window) #ttk.Frame(master = parent)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int) #ttk.Entry(master = parent, textvariable = variable_to_store_input_value_in)
button = ttk.Button(master = input_frame, text = "Convert", command = convert) #ttk.Button(master = parent, text = "Text on Button", command = function_to_perform_on_button_press)
entry.pack(side  = "left", padx = 10)
button.pack(side  = "left")
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window, 
    text = "Output", 
    font = "Calibri 24", 
    textvariable = output_string)
output_label.pack(pady = 5)

# run
window.mainloop()