# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:01:39 2023

Animatsiya

@author: DAVRON
"""

import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
temp = 1
c = ["red","green","blue"]
for i in range(400):
    t.color(c[i%3])
    t.forward(temp)
    t.left(120)
    t.left(1)
    temp=temp+1
turtle.mainlop()