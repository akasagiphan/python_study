#!/usr/bin/env python
# coding: utf-8

# In[8]:


paid_amt = int(input("Nhập tổng giá trị hàng mà bạn đã mua ($): "))
if paid_amt >= 150:
    print("Bạn được giảm $50.")
    print(f"Tổng tiền bạn cần thanh toán sau khi được giảm: ${paid_amt} - $50 = ${paid_amt-50}")
elif paid_amt >= 100:
    print("Bạn được giảm $25.")
    print(f"Tổng tiền bạn cần thanh toán sau khi được giảm: ${paid_amt} - $25 = ${paid_amt-25}")
elif paid_amt >= 75:
    print("Bạn được giảm $15.")
    print(f"Tổng tiền bạn cần thanh toán sau khi được giảm: ${paid_amt} - $15 = ${paid_amt-15}")
else:
    print("Bạn không được giảm giá.")
    print(f"Tổng tiền bạn cần thanh toán: ${paid_amt}")

