#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import turtle

d = int(input("Nhập khoảng cách tối đa cho phép: "))
pen = turtle.Turtle()
n = 0

while pen.distance(0,0) < d:
    pen.right(15)
    pen.forward(n)
    n += 0.1

turtle.done()

