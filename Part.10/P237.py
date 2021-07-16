# -*- coding: utf-8 -*-
# @Time    : 2021/7/16 16:46
# @File    : P237.py
from P236 import Vector_v2


class Vecotr_v3(Vector_v2):
    shorcut_name = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shorcut_name.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in cls.shorcut_name:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attribute 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(attr_name=name, cls_name=cls.__name__)
                raise AttributeError(msg)
        super().__setattr__(name, value)


if __name__ == '__main__':
    v = Vecotr_v3(range(5))
    print(v)
    print(v.x)
    # v.x = 10 # AttributeError: readonly attribute 'x'
