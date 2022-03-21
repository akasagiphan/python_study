#!/usr/bin/env python
# coding: utf-8

# In[14]:


i = True
while i == True:
    a = int(input("Nhập vào số nguyên để kiểm tra chẵn lẻ: "))
    print(f"Số {a} là số chẵn." if not a%2 else f"Số {a} là số lẻ.")
    text = input("Bạn có muốn kiểm trả tiếp? (y/n): ")
    if text != "y":
        print("Kết thúc chương trình!")
        i = False

