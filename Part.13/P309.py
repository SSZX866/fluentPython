# -*- coding: utf-8 -*-
# @Time    : 2021/7/16 17:23
# @File    : P309.py
import itertools
import math
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/Part.10')
from P237 import Vecotr_v3


class Vector_v6(Vecotr_v3):
    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __neg__(self):  # 取反运算符
        return Vector_v6(-x for x in self)

    def __pos__(self):  # 取正运算符
        return Vector_v6(self)

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0, 0)
            return Vector_v6(a + b for a, b in pairs)
        except:
            return NotImplemented

    def __radd__(self, other):
        return self + other


if __name__ == '__main__':
    v = Vector_v6(range(7))
    print(abs(v))
    print(-v)
    print(+v)
