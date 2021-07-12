# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 16:25
# @File    : P155.py

def decorate(func):
    return func


@decorate
def target():
    print('running target()')


target()

# 装饰器效果等价于
print('-' * 50)


def target():
    print('running target()')


target = decorate(target)
target()

print('-' * 50)


def deco(func):
    def inner():
        print('running inner()')

    return inner


@deco
def target():
    print('running target()')


target()  # 调用target运行inner
print(target)  # target被替换为inner函数的引用
