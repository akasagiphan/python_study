#!/usr/bin/env python
# coding: utf-8

# In[5]:


from tkinter import *

windows = Tk()
windows.title("Simple Calculator")
windows.eval('tk::PlaceWindow . center')

expression = ""
equation = StringVar()
expression_field = Entry(windows, textvariable=equation, width = 40)

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)
    
def calc():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""
        
def clear():
    global expression
    expression = ""
    equation.set("")

    
zero_btn = Button(windows, text='0', width=10, command=lambda: press(0))
one_btn = Button(windows, text='1', width=10, command=lambda: press(1))
two_btn = Button(windows, text='2', width=10, command=lambda: press(2))
three_btn = Button(windows, text='3', width=10, command=lambda: press(3))
four_btn = Button(windows, text='4', width=10, command=lambda: press(4))
five_btn = Button(windows, text='5', width=10, command=lambda: press(5))
six_btn = Button(windows, text='6', width=10, command=lambda: press(6))
seven_btn = Button(windows, text='7', width=10, command=lambda: press(7))
eight_btn = Button(windows, text='8', width=10, command=lambda: press(8))
nine_btn = Button(windows, text='9', width=10, command=lambda: press(9))
calc_btn = Button(windows, text='=', width=10, command=calc)
float_btn = Button(windows, text='.', width=10, command=lambda: press("."))
clear_btn = Button(windows, text='Clear', width=10, command=clear)
add_btn = Button(windows, text='+', width=10, command=lambda: press("+"))
minus_btn = Button(windows, text='-', width=10, command=lambda: press("-"))
multiply_btn = Button(windows, text='*', width=10, command=lambda: press("*"))
divide_btn = Button(windows, text='/', width=10, command=lambda: press("/"))

expression_field.grid(row = 0, column = 0, columnspan = 4)
one_btn.grid(row = 1, column = 0)
two_btn.grid(row = 1, column = 1)
three_btn.grid(row = 1, column = 2)
add_btn.grid(row = 1, column = 3)
four_btn.grid(row = 2, column = 0)
five_btn.grid(row = 2, column = 1)
six_btn.grid(row = 2, column = 2)
minus_btn.grid(row = 2, column = 3)
seven_btn.grid(row = 3, column = 0)
eight_btn.grid(row = 3, column = 1)
nine_btn.grid(row = 3, column = 2)
multiply_btn.grid(row = 3, column = 3)
zero_btn.grid(row = 4, column = 0)
clear_btn.grid(row = 4, column = 1)
calc_btn.grid(row = 4, column = 2)
divide_btn.grid(row = 4, column = 3)
float_btn.grid(row = 5, column = 0)

windows.mainloop()

