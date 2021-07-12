# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 17:08
# @File    : p21.py

# 列表推导式 笛卡尔积
colors = ['blacks', 'white']
sizes = ['S', 'M', 'L']

tshirts1 = [(color, size) for color in colors for size in sizes]
print(tshirts1)

tshirts2 = []
for color in colors:
    for size in sizes:
        tshirts2.append((color, size))
print(tshirts2)

# 使用生成器表达式可以减少内存开销
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)
