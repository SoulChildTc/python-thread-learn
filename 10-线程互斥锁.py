from threading import Thread, Lock
import time

n = 100


def task():
    global n
    # mutex.acquire()
    # temp = n
    # time.sleep(0.1)
    # n = temp - 1
    # mutex.release()
    with mutex:
        temp = n
        time.sleep(0.1)
        n = temp - 1


if __name__ == '__main__':
    start_time = time.time()
    mutex = Lock()
    t_l = []
    for i in range(100):
        t = Thread(target=task)
        t_l.append(t)
        t.start()

    for t in t_l:
        t.join()

    print("主", n)
    print(time.time() - start_time)
