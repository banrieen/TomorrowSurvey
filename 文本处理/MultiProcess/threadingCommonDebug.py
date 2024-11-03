#!/usr/bin env python3

import threading
from time import sleep, ctime

# 派生 Thread 的子类，并创建子类的实例
class MyThread(threading.Thread):
    def __init__(self, func, args, name=""):
        # 构造threading.Thread 类
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print("Starting ",self.name, " at: ",ctime())
        self.res = self.func(*self.args)
        print(self.name, " finished ","at: ",ctime())