# -*- coding: utf-8 -*-
# @Time    : 2021/7/14 16:52
# @File    : P210.py
# 格式化字符串
from datetime import datetime

brl = 1 / 2.43

print(brl)
print(format(brl, '0.4f'))
print('1 BRL = {rate:0.2f} USD'.format(rate=brl))

print('-' * 50)
print(format(42, 'b'))  # 转为二进制字符串
print(format(2 / 3, '.1%'))  # 转为百分数

now = datetime.now()
print(format(now, '%H:%M:%S'))  # 17:05:52
print("It's now {:%I:%M %p}".format(now))  # It's now 05:05 PM

print('-' * 50)
from P207 import Vector2d

v1 = Vector2d(3, 4)
print(format(v1))
print(format(v1, '.2f'))
print(format(v1, '.3e'))
