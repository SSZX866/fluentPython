# -*- coding: utf-8 -*-
# @Time    : 2021/7/7 17:41
# @File    : P37.py
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
# 两个结果并不是完全反转，因为sorted是稳定的排序，在len长度相同时，相对位置不会发生改变
