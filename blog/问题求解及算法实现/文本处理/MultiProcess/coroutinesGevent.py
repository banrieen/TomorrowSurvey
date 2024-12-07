import gevent
# Reference: https://www.cnblogs.com/aylin/p/5601969.html

def fun1():
    print("www.baidu.com")   # 第一步
    gevent.sleep(0)
    print("end the baidu.com")  # 第三步

def fun2():
    print("www.zhihu.com")   # 第二步
    gevent.sleep(0)
    print("end th zhihu.com")  # 第四步

gevent.joinall([
    gevent.spawn(fun1),
    gevent.spawn(fun2),
])