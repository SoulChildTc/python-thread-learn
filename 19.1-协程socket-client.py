from socket import *
from threading import current_thread, Thread
import time


def client():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(("127.0.0.1", 8080))
    while 1:
        client.send((current_thread().getName()).encode("utf-8"))
        data = client.recv(1024)
        print(data.decode("utf-8"))


if __name__ == '__main__':
    for i in range(1):
        t = Thread(target=client)
        t.start()
