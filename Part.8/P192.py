# -*- coding: utf-8 -*-
# @Time    : 2021/7/12 22:02
# @File    : P192.py
# 不要使用可变类型作为参数默认值
class HauntedBus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    bus1 = HauntedBus()
    bus1.pick('Alice')
    print(bus1.passengers)  # ['Alice']
    bus2 = HauntedBus()
    print(bus2.passengers)  # ['Alice'] bus1修改的是默认列表，因此创建bus2时会直接生成Alice
