# -*- coding: utf-8 -*-
# @Time    : 2021/7/13 20:20
# @File    : P207.py
from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)  # 直接转为float，尽早捕获数据异常
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))  # 生成器表达式

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)  # 存在缺陷，当Vector2d(2,3)和(2,3)或[2,3]比较时也会返回True

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, format_spec):
        components = (format(c, format_spec) for c in self)
        return '({}, {})'.format(*components)
