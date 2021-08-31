from threading import Thread, Semaphore, current_thread
import time
import random
"""
信号量
信号量用来控制线程并发数的，信号量管理一个内置的计数器,每当调用acquire()时-1,调用release()时+1。
例如threading.Semaphore(5)相当于给定5把锁
每次acquire占用就会-1,release释放就会+1,释放后就会有其他线程来争夺锁
"""

sm = Semaphore(5)


def task():
    sm.acquire()
    print('%s 抢到了锁' % current_thread().getName())
    time.sleep(random.randint(1, 3))
    sm.release()
    print("-- %s 释放了锁 --" % current_thread().getName())


if __name__ == '__main__':
    for i in range(20):
        t = Thread(target=task)
        t.start()

"""
可以看到每释放一次锁，就会有一个新的线程来占用。
"""