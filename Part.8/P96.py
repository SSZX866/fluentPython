# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 22:24
# @File    : P96.py
import weakref

a_set = {0, 1}
wref = weakref.ref(a_set)
print(wref)
print(wref())  # 调用弱引用返回的是被引用的对象，若对象不存在则返回None
a_set = {2, 3, 4}
print(wref())
