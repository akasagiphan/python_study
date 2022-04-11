#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle

pen = turtle.Turtle()
turtle.bgcolor("cyan")
cont = True

def draw_a_house(x,y):
    pen.penup()
    pen.setpos(x-30,y-18)
    pen.pendown()
    pen.fillcolor("yellow")
    pen.begin_fill()
    for i in range(2):
        pen.forward(60)
        pen.left(90)
        pen.forward(36)
        pen.left(90)
    pen.end_fill()
    pen.penup()
    pen.setpos(x-5,y-18)
    pen.pendown()
    pen.fillcolor("black")
    pen.begin_fill()
    for i in range(2):
        pen.forward(10)
        pen.left(90)
        pen.forward(25)
        pen.left(90)
    pen.end_fill()
    pen.penup()
    pen.setpos(x-30,y+18)
    pen.pendown()
    pen.fillcolor("red")
    pen.begin_fill()
    pen.goto(x,y+28)
    pen.goto(x+30,y+18)
    pen.end_fill()

while cont == True:
    x = int(input("Nhập tọa độ x: "))
    y = int(input("Nhập tọa độ y: "))
    draw_a_house(x,y)
    print("Bạn có muốn vẽ thêm nhà? (y/n)")
    more = ""
    while more not in ("y","n"):
        more = str(input("Chọn y hoặc n: "))
    if more == "n":
        cont = False
        turtle.done()

