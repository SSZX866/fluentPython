# -*- coding: utf-8 -*-
# @Time    : 2021/7/16 15:54
# @File    : P231.py
from array import array
import reprlib
import math


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):  # 将Vector变为可迭代对象
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))  # 因为Vector已经是可迭代对象了，因此可以直接转为元组

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    # ---------------------------------------------------------------------------------- #
    # P223 序列化
    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        return self._components[index]


if __name__ == '__main__':
    vector = Vector([3.1, 3.2])
    print(vector)

    print(vector[0], vector[-1])
    v7 = Vector(range(7))
    print(v7[1:4])
