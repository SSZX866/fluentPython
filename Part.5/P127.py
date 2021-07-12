# -*- coding: utf-8 -*-
# @Time    : 2021/7/9 15:50
# @File    : P127.py
import bobo


@bobo.query('/')
def hello(person):
    return 'Hello %s!' % person

# bobo -f P127.py
# http://127.0.0.1:8080/?person=caowei
