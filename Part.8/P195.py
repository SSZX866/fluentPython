# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 22:18
# @File    : P195.py
import weakref

s1 = {1, 2, 3}
s2 = s1


def bye():
    print('Gone with the wind...')


ender = weakref.finalize(s1, bye)
print(ender.alive)
del s1
print(ender.alive)
s2 = 'spam'  # ender拥有{1, 2, 3}的弱引用，弱引用不会增加对象的引用数量，当引用数量归零后对象仍然会被回收
print(ender.alive)
