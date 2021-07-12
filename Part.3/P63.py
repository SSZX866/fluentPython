# -*- coding: utf-8 -*-
# @Time    : 2021/7/8 16:18
# @File    : P63.py

class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d[4])
# print(d[1])
print(d.get(1, 'not found'))
print(2 in d, '2' in d)
