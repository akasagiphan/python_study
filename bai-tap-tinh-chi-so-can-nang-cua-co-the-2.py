#!/usr/bin/env python
# coding: utf-8

# In[5]:


h = float(input("Nhập chiều cao (m): "))
w = int(input("Nhập cân nặng (kg): "))
bmi = w/(h**2)
if bmi > 40:
    print(f"Chỉ số BMI = {bmi}: Béo phì cấp độ III")
elif 35 <= bmi < 40:
    print(f"Chỉ số BMI = {bmi}: Béo phì cấp độ II")
elif 30 <= bmi < 35:
    print(f"Chỉ số BMI = {bmi}: Béo phì cấp độ I")
elif 25 <= bmi < 30:
    print(f"Chỉ số BMI = {bmi}: Thừa cân")
elif 18.5 <= bmi < 25:
    print(f"Chỉ số BMI = {bmi}: Bình thường")
elif 17 <= bmi < 18.5:
    print(f"Chỉ số BMI = {bmi}: Gầy cấp độ I")
elif 16 <= bmi < 17:
    print(f"Chỉ số BMI = {bmi}: Gầy cấp độ II")
else:
    print(f"Chỉ số BMI = {bmi}: Gầy cấp độ III")

