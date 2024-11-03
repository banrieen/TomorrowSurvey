#!/usr/bin env python3
from threadingCommonDebug import MyThread
from time import sleep, ctime

def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def fact(x):
    sleep(0.1)
    if x < 2:
        return 1
    else:
        return x * fact(x-1)

def sum(x):
    sleep(0.1)
    if x < 2:
        return 1
    else:
        return sum(x-1) + x

funcs = [fib, fact, sum]
n = 15

def main():
    nfuncs = range(len(funcs))
    print("SINGLE Thread")
    for i in nfuncs:
        print("Starting ", funcs[i].__name__, " at: ", ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, " finished at: ", ctime())

    print("MULTIPLE THREAD")
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i],(n,),funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())

    print('All Done ')

if __name__ == "__main__":
    main()