#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle

pen = turtle.Turtle()
turtle.bgcolor("cyan")

def draw_a_house(x,y,house_color,door_color,roof_color):
    pen.penup()
    pen.setpos(-x/2,0)
    pen.pendown()
    pen.fillcolor(house_color)
    pen.begin_fill()
    for i in range(2):
        pen.forward(x)
        pen.left(90)
        pen.forward(y)
        pen.left(90)
    pen.end_fill()
    pen.penup()
    pen.setpos(-x/10,0)
    pen.pendown()
    pen.fillcolor(door_color)
    pen.begin_fill()
    for i in range(2):
        pen.forward(x/5)
        pen.left(90)
        pen.forward(y/2)
        pen.left(90)
    pen.end_fill()
    pen.penup()
    pen.setpos(-x/2,y)
    pen.pendown()
    pen.fillcolor(roof_color)
    pen.begin_fill()
    pen.goto(0,y*1.5)
    pen.goto(x/2,y)
    pen.end_fill()
    
def draw_a_tree(leaf_color,z):
    pen.penup()
    pen.setpos(-x*1.2,0)
    pen.pendown()
    pen.fillcolor("brown")
    pen.begin_fill()
    for i in range(2):
        pen.forward(20)
        pen.left(90)
        pen.forward(50)
        pen.left(90)
    pen.end_fill()
    n = 50
    pen.right(180)
    for i in range(z):
        n += 40
        pen.penup()
        pen.setpos(-x*1.2+10,n)
        pen.pendown()
        pen.fillcolor(leaf_color)
        pen.begin_fill()
        pen.circle(30,steps = 3)
        pen.end_fill()
    
x = int(input("Nhập độ dài ngang nhà: "))
y = int(input("Nhập độ dài dọc nhà: "))
house_color = str(input("Nhập màu nhà (VD: yellow): "))
door_color = str(input("Nhập màu cửa (VD: black): "))
roof_color = str(input("Nhập màu mái (VD: red): "))
draw_a_house(x,y,house_color,door_color,roof_color)

leaf_color = str(input("Nhập màu tán lá (VD: green): "))
z = int(input("Nhập số lượng tán lá: "))
draw_a_tree(leaf_color,z)

turtle.done()

