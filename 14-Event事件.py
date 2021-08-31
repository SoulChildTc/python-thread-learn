from threading import Thread, Event, current_thread
import time
import random

"""
event = Event() # 这个对象内部有个私有属性_flag,默认是False
event.wait() # 如果_flag值是false,就会阻塞住,等待它变成True,然后再执行后面的代码
event.set() # 把_flag里面的值改为 True
event.clear() # 把_flag里面的值改为 False
"""

event = Event()

"""模拟裁判说Go以后，车开始发动。"""


def referee():
    """裁判"""
    sec = 3
    while sec >= 0:
        if sec == 0:
            print("\nGo")
            # 设置event=True
            event.set()
            break
        print("\r预备%s" % sec, end="")
        time.sleep(1)
        sec -= 1


def car():
    """车"""
    # 当event=True时，往下执行，否则一直等待到event=True
    event.wait()
    time.sleep(random.randint(1, 3))
    print("%s 出发了" % current_thread().getName())


if __name__ == '__main__':
    # 1个裁判
    r = Thread(target=referee)
    r.start()
    # 10个赛车
    for i in range(10):
        t = Thread(target=car)
        t.start()
