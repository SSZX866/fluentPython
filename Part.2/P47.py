# -*- coding: utf-8 -*-
# @Time    : 2021/7/8 15:29
# @File    : P47.py

from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)

dq.rotate(3)
print(dq)

dq.rotate(-4)
print(dq)

dq.appendleft(-1)
print(dq)

dq.extend([11, 22, 33])
print(dq)

dq.extendleft([10, 20, 30, 40])
print(dq)
