#!/usr/bin env python3

import threading
from time import sleep, ctime

def loop(nloop, nsec):
    print('Start loop: ', nloop, ' at ',ctime())
    sleep(nsec)
    print('loop ',nloop, ' done at: ',ctime())

# 函数调用
def main():
    loops = [4,2]
    print('Starting at: ',ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)
    
    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all done at: ',ctime())

# 使用 Thread 的类实例，传给它一个可调用的类实例
class ThreadFunc(object):
    def __init__(self, func, args, name=""):
        self.name = name
        self.func = func
        self.args = args
        
    def __call__(self):
        self.func(*self.args)

def main_class_object():
    loops = [4,2]
    print('Starting at: ',ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]),loop.__name__))
        threads.append(t)
    
    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all done at: ',ctime())

# 派生 Thread 的子类，并创建子类的实例
class MyThread(threading.Thread):
    def __init__(self, func, args, name=""):
        # 构造threading.Thread 类
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        self.func(*self.args)

def main_child_class_object():
    loops = [4,2]
    print('Starting at: ',ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]),loop.__name__)
        threads.append(t)
    
    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all done at: ',ctime())

if __name__ == "__main__":
    """ Target 为函数调用 """
    # main()
    """ Target 为类实例调用 """
    # main_class_object()
    """ Target 为子类的实例调用 """
    main_child_class_object()
