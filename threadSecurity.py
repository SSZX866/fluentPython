# -*- coding: utf-8 -*-
# @Time    : 2021/7/8 14:26
# @File    : threadSecurity.py
import threading
import time


class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self.balance = balance


# 定义一个函数来模拟取钱操作
def draw(account, draw_amount):
    # 账户余额大于取钱数目
    if account.balance >= draw_amount:
        # 吐出钞票
        print(threading.current_thread().name + "取钱成功！吐出钞票:" + str(draw_amount))
        # time.sleep(0.001)
        # 修改余额
        account.balance -= draw_amount
        print("\t余额为: " + str(account.balance))
    else:
        print(threading.current_thread().name + "取钱失败！余额不足！")


# 创建一个账户
acct = Account("1234567", 1000)
# 模拟两个线程对同一个账户取钱
t1 = threading.Thread(name='甲', target=draw, args=(acct, 800))
t2 = threading.Thread(name='乙', target=draw, args=(acct, 800))
t1.start()
t2.start()
t1.join()
t2.join()

print('-' * 50)


class Account:
    # 定义构造器
    def __init__(self, account_no, balance):
        # 封装账户编号、账户余额的两个成员变量
        self.account_no = account_no
        self.balance = balance
        self.lock = threading.RLock()

    def drawWithLock(self, account, draw_amount):
        # 账户余额大于取钱数目

        self.lock.acquire()
        try:
            if account.balance >= draw_amount:
                # 吐出钞票
                print(threading.current_thread().name + "取钱成功！吐出钞票:" + str(draw_amount))
                # time.sleep(0.001)
                # 修改余额
                account.balance -= draw_amount
                print("\t余额为: " + str(account.balance))
            else:
                print(threading.current_thread().name + "取钱失败！余额不足！")
        finally:
            self.lock.release()


acct = Account("1234567", 1000)
# 模拟两个线程对同一个账户取钱
threading.Thread(name='甲', target=acct.drawWithLock, args=(acct, 800)).start()
threading.Thread(name='乙', target=acct.drawWithLock, args=(acct, 800)).start()