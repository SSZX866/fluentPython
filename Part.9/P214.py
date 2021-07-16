# -*- coding: utf-8 -*-
# @Time    : 2021/7/14 17:14
# @File    : P214.py
# 可散列的Vector2d
from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)  # 直接转为float，尽早捕获数据异常
        self.__y = float(y)  # 使用双下划线前导将属性标记为私有

    def __iter__(self):
        return (i for i in (self.__x, self.__y))  # 生成器表达式

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)  # 存在缺陷，当Vector2d(2,3)和(2,3)或[2,3]比较时也会返回True

    def __abs__(self):
        return math.hypot(self.__x, self.__y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, format_spec):
        components = (format(c, format_spec) for c in self)
        return '({}, {})'.format(*components)

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    @property  # property装饰器将读值方法标记为特性
    def x(self):  # 读值方法与公开属性同名
        return self.__x

    @property
    def y(self):
        return self.__y

    def __hash__(self):  # 最好使用异或混合分量的散列值
        return hash(self.x) ^ hash(self.y)


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    v2 = Vector2d(3.1, 4.2)
    print(v1.x)
    print(hash(v1), hash(v2))
    print({v1, v2})
