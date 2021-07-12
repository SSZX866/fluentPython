# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 16:37
# @File    : P156.py

registry = []


def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    # 装饰器在导入模块后立即运行
    # running register(<function f1 at 0x7fa16449adc0>)
    # running register(<function f2 at 0x7fa1679f95e0>)
    print('running main()')
    print('registry ->', registry)  # registry -> [<function f1 at 0x7fa16449adc0>, <function f2 at 0x7fa1679f95e0>]
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()
