#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Hello World! Tkinter GUI app that closes itself after 5 seconds.
"""
import tkinter as tk


root = tk.Tk()
print(root.getvar("tk_version"))

label = tk.Label(root, text="Hello World!")
label.pack(padx=20, pady=20)

# Close the Window after 5 seconds
root.after(5000, root.destroy)

root.mainloop()
