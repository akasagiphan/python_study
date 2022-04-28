#!/usr/bin/env python
# coding: utf-8

# In[31]:


from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Weight converter")

w_kg_lbl = Label(window, text = "Enter the weight in kg:")
w_kg = Entry(window)
w_gram_lbl = Label(window, text = "Gram")
w_pounds_lbl = Label(window, text = "Pounds")
w_ounce_lbl = Label(window, text = "Ounce")
w_gram_result_lbl = Label(window, text = 0)
w_pounds_result_lbl = Label(window, text = 0)
w_ounce_result_lbl = Label(window, text = 0)

def convert_from_kg():
    if w_kg.get() == "":
        messagebox.showwarning("Error", "Please input a value!")
    elif w_kg.get() != "":
        try:
            x = float(w_kg.get())
        except:
            messagebox.showwarning("Error", "Please input a valid value!")
        finally:
            w_gram = round(float(w_kg.get())*1000,3)
            w_pounds = round(float(w_kg.get())*2.20462,3)
            w_ounce = round(float(w_kg.get())*35.274,3)
            w_gram_result_lbl.config(text = w_gram)
            w_pounds_result_lbl.config(text = w_pounds)
            w_ounce_result_lbl.config(text = w_ounce)

convert_btn = Button(window, text = "Convert", command = convert_from_kg)
    
w_kg_lbl.grid(row = 0, column = 0)
w_kg.grid(row = 0, column = 1)
convert_btn.grid(row = 0, column = 2)
w_gram_lbl.grid(row = 1, column = 0)
w_pounds_lbl.grid(row = 1, column = 1)
w_ounce_lbl.grid(row = 1, column = 2)
w_gram_result_lbl.grid(row = 2, column = 0)
w_pounds_result_lbl.grid(row = 2, column = 1)
w_ounce_result_lbl.grid(row = 2, column = 2)

window.mainloop()

