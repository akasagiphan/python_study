#!/usr/bin/env python
# coding: utf-8

# In[4]:


i = True
while i == True:
    a = float(input("Nhập vào số a bất kì: "))
    if a % 2 == 0:
        print('Số a là số chẵn.')
    elif a % 2 == 1:
        print('Số a là số lẻ.')
    else:
        print('Số a không phải số tự nhiên!')
    text = input("Bạn có muốn kiểm tra số khác? (y/n): ")
    if text != "y":
        i = False
        print("Chương trình kết thúc!")

