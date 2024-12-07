#!/usr/bin/env python3
# python3 中 thread => _thread
# Python 核心编程第三版，多线程
import _thread
from time import sleep, ctime

def loop0():
    print('Start loop 0 at: ',ctime())
    sleep(4)
    print('Loop 0 done at: ',ctime())


def loop1():
    print('Start loop 1 at: ',ctime())
    sleep(2)
    print('Loop 1 done at: ',ctime())

def main():
    print('Start at: ',ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(6)
    print('All Done at: ',ctime())


# 采用同步锁

def loop_lock(nloop, nsec, lock):
    print('Start loop: ', nloop, ' at ',ctime())
    sleep(nsec)
    print('loop ',nloop, ' done at: ',ctime())
    lock.release()

def _main():
    loops = [4,2]
    print('Starting at: ',ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    
    for i in nloops:
        _thread.start_new_thread(loop_lock,(i, loops[i], locks[i]))

    for i in nloops:
        while locks[i].locked():
            pass

    print('all done at: ',ctime())

if __name__ == "__main__":
    _main()