#!/usr/bin/env python
# coding: utf-8

# In[15]:


def get_min_numbers(numbers):
    result = numbers[0]
    for num in numbers:
            if result > num:
                result = num
    return result

numbers = []
finished = False
while finished == False:
    a = int(input("Nhập giá trị muốn đưa vào list: "))
    numbers.append(a)
    print(f"List hiện tại: numbers = {numbers}.")
    print("------------------------------")
    b = ""
    while b not in ("y","n"):
        b = str(input("Bạn có muốn tiếp tục thêm số? (y/n): "))
        print("------------------------------")
    if b == "n":
        finished = True

min_number = get_min_numbers(numbers)
print("Số nhỏ nhất là:", min_number)

