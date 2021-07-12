# -*- coding: utf-8 -*-
# @Time    : 2021/7/8 19:56
# @File    : P120.py
def reverse(word):
    return word[::-1]


fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))
print(sorted(fruits, key=reverse))
