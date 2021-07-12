# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 16:57
# @File    : P162.py

class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)


avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))

print('-' * 50)


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        # 这里series对averager函数来说是自由变量，虽然定义函数(make_averager)已经返回结果了，series作用域已不可用
        # 但是averager会保留定义函数存在的自由变量的绑定，
        total = sum(series)
        return total / len(series)

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
print(avg.__code__.co_varnames, avg.__code__.co_freevars)

# __closure__中各个元素对应__code__.co_freevars自由变量中的元素，cell_contents属性中存储着真正的值
for i in range(len(avg.__code__.co_freevars)):
    print(avg.__code__.co_freevars[i] + ':', avg.__closure__[i].cell_contents)

print('-' * 50)


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count # nonloacl 可以把变量标记为自由变量
        nonlocal total
        total += new_value
        count += 1
        return total / count

    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))
