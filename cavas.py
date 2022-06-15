#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 19:21:05 2022

@author: clockshield
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Planet Encyclopedia")
root.geometry("500x500")
root.config(bg="lightblue")

color_label=Label(root, text = "Enter a color: ")
color_label.place(relx = 0.6, rely = 0.9, anchor = CENTER)

input_box = Entry(root)
input_box.insert(0, "black")
input_box.place(relx = 0.8, rely = 0.9, anchor = CENTER)


canvas = Canvas(root, width = 590, height = 510, bg = "white", highlightbackground = "lightgray")
canvas.pack()

direction = ""
oldx = 50
oldy = 50
newx = 50
newy = 50

def draw( direction, oldx, oldy, newx, newy):
    fill_color = input_box.get()
    
    
root.bind("<Right>", right_dir)
root.bind("<Left>", left_dir)
root.bind("<Up>", up_dir)
root.bind("<Down>", down_dir)

root.mainloop()