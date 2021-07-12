# -*- coding: utf-8 -*-
# @Time    : 2021/7/8 15:53
# @File    : P56.py

# 只有可散列的数据类型才能作为映射的键

tt = (1, 2, (30, 40))
print(hash(tt))
tt = (1, 2, [30, 40])
# print(hash(tt))
tt = (1, 2, frozenset([30, 40]))
print(hash(tt))

print('-' * 50)
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict((('one', 1), ('two', 2), ('three', 3)))
e = {key: value for key, value in [('one', 1), ('two', 2), ('three', 3)]}
print(a == b == c == d == e)