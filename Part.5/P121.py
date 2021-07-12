# -*- coding: utf-8 -*-
# @Time    : 2021/7/8 19:58
# @File    : P121.py
from functools import reduce


def factorial(n):
    if n < 0: return
    return 1 if n == 0 else factorial(n - 1) * n


print(list(map(factorial, range(6))))
print([factorial(i) for i in range(6)])

print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
print([factorial(n) for n in range(6) if n % 2])

print('-' * 50)
# 规约函数
# reduce 累计结果 all 全部为真 结果为真 any 有一个为真 结果为真
print(reduce(lambda x, y: x + factorial(y), [0] + list(range(5))))
print(sum(factorial(n) for n in range(5)))
print(all([1, True, 'abc']))
print(all([1, True, 'abc', ()]))
print(any([[], '', 0]))
print(any([[], '', 0, {1}]))
