# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 16:19
# @File    : p8.py
import math


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __bool__(self):
        return bool(self.x or self.y)


v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)

v = Vector(3, 4)
print(abs(v))

print(v * 3)
print(abs(v * 3))
print(v)
