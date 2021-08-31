"""
守护进程(daemon)是一类在后台运行的特殊进程，用于执行特定的系统任务。
当子进程执行的任务在父进程代码运行完毕后就没有存在的必要了,那么该子进程个就应该被设置为守护进程
"""
from multiprocessing import Process
import time


# # 用法
# def task(name):
#     print("%s is running" % name)
#     time.sleep(2)
#     print("%s is done" % name)
#
#
# if __name__ == '__main__':
#     p = Process(target=task, args=("soulchild",))
#     # 将p这个进程设置为守护进程,设置后主进程结束，子进程也直接结束。
#     p.daemon = True
#     p.start()
#     print('master')


# 下面代码print("master")结束后,守护进程也会结束
def foo():
    print("123开始")
    time.sleep(1)
    print("123结束")


def bar():
    print("456开始")
    time.sleep(3)
    print("456结束")


if __name__ == '__main__':
    p1 = Process(target=foo)
    p2 = Process(target=bar)
    p1.daemon = True
    p1.start()
    p2.start()
    # 加上这个延迟后123开始会执行,print("master")执行后,p1守护进程也会结束
    time.sleep(0.001)
    print('master')
