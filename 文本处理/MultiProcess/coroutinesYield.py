""" Python3 coroutines 协程实现方式 """

""" # native by yield
def consume():
    number = (yield)
    print("开始消费： ", number)

consumer = consume()

next(consumer)

for num in range(0,100):
    print("开始生产： ", num)
    # 发送数据给 consumer 协程
    consumer.send(num) """

import time

def A():
    while 1:
        print('------A-----')
        time.sleep(0.1)
        yield()

def B():
    while 1:
        print('-------B-----')
        time.sleep(0.1)
        next(a)

a = A()
B()
    