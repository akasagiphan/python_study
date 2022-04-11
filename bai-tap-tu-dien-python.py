#!/usr/bin/env python
# coding: utf-8

# In[41]:


def trungle_translator(word):
    dic = {"apple":"quả táo",
           "orange":"quả cam",
           "lemon":"quả chanh",
           "pear":"quả lê",
           "peach":"quả đào"}
    translated_word = ""
    for en_word, vi_word in dic.items():
        if en_word == word:
            translated_word = vi_word
    if translated_word == "":
        print("Từ không tồn tại trong từ điển!")
    else:
        print(f"Từ nhập vào: [{word}] có nghĩa là: [{translated_word}]")
        
input_word = str(input("Nhập vào từ cần tra: "))
print("-------------------------------------------")
trungle_translator(input_word)

