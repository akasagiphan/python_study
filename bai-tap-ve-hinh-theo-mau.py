#!/usr/bin/env python
# coding: utf-8

# In[40]:


import turtle

pen = turtle.Turtle()
i = 0
turtle.bgcolor("black")

while i < 24:
    pen.right(15)
    if i%6 == 0:
        pen.color("red")
    elif i%6 == 1:
        pen.color("green")
    elif i%6 == 2:
        pen.color("blue")
    elif i%6 == 3:
        pen.color("yellow")
    elif i%6 == 4:
        pen.color("magenta")
    else:
        pen.color("cyan")
    j = 0
    while j < 2:
        pen.circle(120,90)
        pen.circle(60,90)
        j += 1
    i += 1
turtle.done()

