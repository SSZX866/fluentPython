# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 20:47
# @File    : P174.py
# 装饰器若想传参，必须使用闭包作工厂函数

registry = set()


def register(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func

    return decorate


@register(active=False)
def f1():
    print('running f1()')


@register()
def f2():
    print('running f2()')


def f3():
    print('running f3()')

if __name__ == '__main__':
    print(registry)
    print(register()(f3))
    print(registry)
    print(register(active=False)(f2))
    print(registry)