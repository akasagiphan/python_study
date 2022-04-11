#!/usr/bin/env python
# coding: utf-8

# In[8]:


print("**********************")
print("BẢNG CỬU CHƯƠNG TỪ 1-9")
print("**********************")

for number in range(1,10):
    print(f"  Bảng cửu chương {number}:")
    for i in range(1,10):
        print("    " + str(number) + ' x ' + str(i) + ' = ' + str(number*i))

