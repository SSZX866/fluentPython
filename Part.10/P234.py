# -*- coding: utf-8 -*-
# @Time    : 2021/7/16 16:24
# @File    : P234.py
# 切片原理
class MySeq:
    def __getitem__(self, index):
        return index


if __name__ == '__main__':
    s = MySeq()
    print(s[1])
    print(s[1:4])
    print(s[1:4:2])
    print(s[1:4:2, 9])  # (slice(1, 4, 2), 9)
    print(s[1:4:2, 7:9])  # (slice(1, 4, 2), slice(7, 9, None))