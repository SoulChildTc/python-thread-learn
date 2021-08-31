from threading import Thread
import time


def piao(name, n):
    print('%s is piaoing' % name)
    time.sleep(n)
    print('%s is piao end' % name)


# 守护线程在所有非守护线程运行完毕就直接结束
if __name__ == '__main__':
    t1 = Thread(target=piao, args=("t1", 3))
    t2 = Thread(target=piao, args=("t2", 1))
    t1.daemon = True
    t1.start()
    t2.start()
    print('mainThread主')

# t1是守护线程，只要主线程和t2线程执行完毕，t1直接就结束掉
