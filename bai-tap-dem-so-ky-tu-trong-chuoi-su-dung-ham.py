#!/usr/bin/env python
# coding: utf-8

# In[6]:


def count_chars(txt):
    result = 0
    for char in txt:
        result += 1
    return result

input_str = input('Your string:')

print('Length:', count_chars(input_str))

