#!/usr/bin/env python
# coding: utf-8

# In[22]:


rng = str(input("Nhập khoảng số với định dạng: số bắt đầu,số kết thúc: "))
a = rng.split(",")

while (rng.find(",") == -1) or (a[0] >= a[1]):
    print("Lỗi: Thông tin nhập vào không hợp lệ" if rng.find(",") == -1 else "Lỗi: Kiểm tra giá trị bắt đầu & kết thúc!")
    print("-------------------------------------------")
    rng = str(input("Nhập khoảng số với định dạng: số bắt đầu,số kết thúc: "))
    a = rng.split(",")

x = int(a[0])
y = int(a[1])
print("-------------------------------------------")
print("Chuỗi giá trị FizzBuzz:")
for i in range(x,y+1):
    if not i%15:
        print("FizzBuzz")
    elif not i%5:
        print("Buzz")
    elif not i%3:
        print("Fizz")
    else:
        print(i)

