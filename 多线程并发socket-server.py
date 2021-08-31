from socket import *
from threading import Thread, current_thread


def server():
    print("主线程:%s" % (current_thread().getName()))
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(("127.0.0.1", 8080))
    server.listen(5)
    while True:
        conn, addr = server.accept()
        print(addr)
        t = Thread(target=comunicate, args=(conn,))
        t.start()


def comunicate(conn):
    print("子线程:%s" % (current_thread().getName()))
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            conn.send(data.upper())
        except ConnectionResetError:
            break
    conn.close()


if __name__ == '__main__':
    server()
