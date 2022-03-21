#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle

nha = turtle.Turtle()

nha_rong = int(input("Nhập chiều rộng căn nhà (khuyến khích 150-200): "))
nha_cao = int(input("Nhập chiều cao căn nhà (khuyến khích 100-150): "))
mau_nha = str(input("Nhập màu nhà (red/green/blue/yellow): "))
mai_cao = int(input("Nhập chiều cao mái nhà (khuyến khích 50-100): "))
mau_mai = str(input("Nhập màu nhà (red/green/blue/yellow): "))

goc_cay = int(input("Nhập chiều rộng thân cây (khuyến khích 20-50): "))
than_cay = int(input("Nhập chiều cao thân cây (khuyến khích 100-150): "))
tan_la = int(input("Nhập số tán lá (khuyến khích < 10): "))

nha.penup()
nha.forward(-nha_rong/2)
nha.pendown()
nha.fillcolor(mau_nha)
nha.begin_fill()
for i in range(2):
    nha.forward(nha_rong)
    nha.left(90)
    nha.forward(nha_cao)
    nha.left(90)
nha.end_fill()
nha.penup()
nha.left(90)
nha.forward(nha_cao)
nha.pendown()
nha.fillcolor(mau_mai)
nha.begin_fill()
nha.goto(0,mai_cao+nha_cao)
nha.goto(nha_rong/2,nha_cao)
nha.end_fill()
nha.penup()
nha.goto(-nha_rong/8,0)
nha.right(90)
nha.pendown()
nha.fillcolor("black")
nha.begin_fill()
for i in range(2):
    nha.forward(nha_rong/4)
    nha.left(90)
    nha.forward(nha_cao/2)
    nha.left(90)
nha.end_fill()

nha.penup()
nha.goto(-nha_rong,0)
nha.pendown()
nha.fillcolor("brown")
nha.begin_fill()
for i in range(2):
    nha.forward(goc_cay)
    nha.left(90)
    nha.forward(than_cay)
    nha.left(90)
nha.end_fill()

nha.penup()
nha.left(90)
nha.forward(than_cay)
nha.right(90)
nha.forward(goc_cay/2)
nha.right(90)
nha.forward(-goc_cay/2)
nha.right(90)
for i in range(tan_la):
    nha.penup()
    nha.pendown()
    nha.fillcolor("green")
    nha.begin_fill()
    nha.circle(goc_cay*1.5,steps = 3)
    nha.end_fill()
    nha.penup()
    nha.right(90)
    nha.forward(goc_cay*1.2)
    nha.left(90)
    nha.pendown()

turtle.bgcolor("cyan")
turtle.done()

