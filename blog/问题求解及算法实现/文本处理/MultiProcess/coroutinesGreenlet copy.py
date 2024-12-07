from greenlet import greenlet
import time

def A():
    while 1:
        print('-------A-------')
        time.sleep(0.5)
        g2.switch()

def B():
    while 1:
        print('-------B-------')
        time.sleep(0.5)
        g1.switch()

g1 = greenlet(A)  #创建协程g1
g2 = greenlet(B)

g1.switch()  #跳转至协程g1