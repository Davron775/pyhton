# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:01:39 2023

Turtle kutibxonasi bilan tanishuv 

turtle-"toshbaqa degan ma'noni anglatadi!"

@author:" DAVRON
"""
""" Turtle kutibxonasi orqali har xil prayektlar """
import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0.5)
temp = 1
c = ["blue","green","white"]
for i in range(500):
    t.color(c[i%3])
    t.forward(temp)
    t.left(120)
    t.left(1)
    temp=temp+1
turtle.mainlop()





""" Gul rasmini pyhton dasturi orqaliu chizish"""
from turtle import *

def fleur():
     for i in range(300):
         circle(190-i,90)
         left(90)
         circle(190-i,90)
         left(18)
         speed(0.5)
         
         
fleur()
mainloop()


























