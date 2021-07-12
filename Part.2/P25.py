# -*- coding: utf-8 -*-
# @Time    : 2021/7/6 17:22
# @File    : P25.py

# *处理多余的拆包元素
a, b, *rest = range(5)
print(a, b, rest)

a, *rest, b = range(5)
print(a, rest, b)

a, b, *rest = range(2)
print(a, b, rest)

# a,*b,*rest = range(6) 只能出现一个*赋值
print('-' * 50)
# 嵌套元组解包
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.43333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'Br', 19.649, (-23.54778, -46.635833))
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:
    # 打印西半球的城市
    if longitude <= 0:
        print(fmt.format(name, latitude, longitude))
