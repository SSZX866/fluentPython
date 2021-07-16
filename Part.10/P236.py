# -*- coding: utf-8 -*-
# @Time    : 2021/7/16 16:30
# @File    : P236.py
import numbers

from P231 import Vector


class Vector_v2(Vector):
    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))


if __name__ == '__main__':
    v7 = Vector_v2(range(7))
    print(v7[-1])
    print(v7[1:4])
    print(v7[-1:])
    print(v7[1, 2])  # TypeError: Vector_v2 indices must be integers
