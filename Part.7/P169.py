# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 20:37
# @File    : P169.py
import functools
from P165 import clock

@clock
@functools.lru_cache()
# @functools.lru_cache()
# @clock
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci_lru(6))
    print('-' * 50)
    print(fibonacci(6))
