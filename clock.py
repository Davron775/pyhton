# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:11:03 2023

@author: DAVRON
"""

from tkinter import *

from tkinter.ttk import *

from time import strftime

main = Tk()

main.title('Pythonda raqamli soat')

def clock():
    tick = strftime('%H:%M:%S') 
    clock_label .config(text =tick)
    clock_label .after(1000,clock)
clock_label = Label(main,font = ('sans',120), background='black',foreground='white')
clock_label.pack(anchor='center')
clock()
mainloop()