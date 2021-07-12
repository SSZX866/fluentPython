# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 20:58
# @File    : P175.py
# 参数化clock装饰器
import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


# 参数化装饰器的工厂函数
def clock(fmt=DEFAULT_FMT):
    # 真正的装饰器
    def decorate(func):
        # 被装饰的函数
        def clocked(*_args):
            t0 = time.time()
            # 被装饰函数真正的结果
            _result = func(*_args)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))  # **locals()为了在fmt中引用clocked的局部变量
            # print(locals()) **为字典解引用
            return result

        return clocked

    return decorate


if __name__ == '__main__':
    @clock()
    def snooze(seconds):
        time.sleep(seconds)


    # clock()(snooze(seconds))
    # decorate(snooze(seconds))
    # clocked(seconds)
    # result
    for i in range(3):
        snooze(.123)

    print('-' * 50)


    @clock('{name}:{elapsed:0.2f}s')
    def snooze(seconds):
        time.sleep(seconds)


    for i in range(3):
        snooze(.123)
