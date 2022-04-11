#!/usr/bin/env python
# coding: utf-8

# In[27]:


a = []
cont = True

while len(a) < 2:
    print("Số lượng phần tử hiện tại chưa đủ. Bạn có muốn thêm số vào list? (y/n)")
    more = ""
    while more not in ("y","n"):
        more = str(input("Nhập y hoặc n: "))
    if more == "y":
        print("---------------------------------------------------")
        a.append(int(input("Nhập số nguyên để đưa vào list: ")))
        print("---------------------------------------------------")
    else:
        print("---------------------------------------------------")
        print("Chương trình kết thúc vì không đủ số lượng phần tử!")
        cont = False
        break

while cont == True:
    print("Số lượng phần tử hiện tại đã đủ. Bạn có muốn thêm số vào list? (y/n)")
    more = ""
    while more not in ("y","n"):
        more = str(input("Nhập y hoặc n: "))
    if more == "y":
        print("---------------------------------------------------")
        a.append(int(input("Nhập số nguyên để đưa vào list: ")))
        print("---------------------------------------------------")
    else:
        cont = False
        print("---------------------------------------------------")
        print(f"List hiện tại bao gồm: {a}")
        print("---------------------------------------------------")
        a.sort()
        print(f"Số có giá trị lớn nhất: {a[-1]}")
        print(f"Số có giá trị lớn nhì: {a[-2]}")

