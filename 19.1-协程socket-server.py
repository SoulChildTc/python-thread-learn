from gevent import socket, spawn, monkey
from threading import current_thread

monkey.patch_all()


def server():
    print("主线程:%s" % (current_thread().getName()))
    server = socket.socket()
    server.bind(("127.0.0.1", 8080))
    server.listen(5)
    while True:
        # 阻塞 等待连接
        conn, addr = server.accept()
        print(addr)
        # 创建协程任务,完后循环到上面的阻塞,遇到IO就会切换,等切换到这个任务的时候就会执行communicate
        spawn(communicate, conn)


def communicate(conn):
    """有连接进来就后处理相应的内容并返回"""
    print("协程:%s" % (current_thread().getName()))
    while True:
        try:
            # 阻塞
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()


if __name__ == '__main__':
    # 创建一个协程任务，gevent遇到IO,就会切换执行协程任务
    g1 = spawn(server)
    # 一直阻塞在这里,直到g1运行完毕
    g1.join()
