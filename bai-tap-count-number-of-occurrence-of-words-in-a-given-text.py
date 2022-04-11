#!/usr/bin/env python
# coding: utf-8

# In[19]:


# Bài làm không dùng count như hướng dẫn nhưng đảm bảo đúng đề bài là dùng hàm và for ... in ...

def count_words(text):
    invalid_char = ",._-!@#$%^&*()"
    for i in invalid_char:
        text = text.replace(i," ")
    text = text.lower()
    text_list = text.split(" ")
    num_words = {}
    for i in range(len(text_list)):
        num_words[text_list[i]] = text.count(text_list[i])
    del num_words[""]
    print(num_words)

message = str(input("Nhập chuỗi văn bản: "))
count_words(message)

