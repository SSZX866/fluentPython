# -*- coding: utf-8 -*-
# @Time    : 2021/7/8 16:43
# @File    : P69.py
import time

t1 = time.time()
needles, haystack = set(range(0, 300000, 5)), set(range(0, 10000000, 3))
print(len(needles & haystack), time.time() - t1)

t2 = time.time()
cnt = 0
for each in haystack:
    if each in needles:
        cnt += 1
print(cnt, time.time() - t2)
