""" Python selector module demo
This module allows high-level and efficient I/O multiplexing, built upon the select module primitives. Users are encouraged to use this module instead, unless they want precise control over the OS-level primitives used.

It defines a BaseSelector abstract base class, along with several concrete implementations (KqueueSelector, EpollSelector…), that can be used to wait for I/O readiness notification on multiple file objects. In the following, “file object” refers to any object with a fileno() method, or a raw file descriptor. See file object.

DefaultSelector is an alias to the most efficient implementation available on the current platform: this should be the default choice for most users.
 """

import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = socket.accept()
    prrint('accepted', conn, 'from ',addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1000) # 准备操作
    if data:
        print('echoing ',repr(data), ' to ', conn)
        conn.send(data) # 该发送uihao不要被阻塞
    else:
        print("closing", conn)
        sel.unregister(conn)
        conn.close()
sock = socket.socket()
sock.bind(('127.0.0.1', 1234))
sock.listen(100)
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)