"""
多个进程之间数据不共享
"""
from multiprocessing import Process
import time


# 方式一
def task(name):
    print("%s is running" % name)
    time.sleep(2)
    print("%s is done" % name)


if __name__ == '__main__':
    p = Process(target=task, args=("soulchild",))
    p.start()
    print('master')


# 方式二
# 继承Process类
# class MyProcess(Process):
#     def __init__(self, name):
#         super(MyProcess, self).__init__()
#         self.name = name
#
#     def run(self):
#         print("%s is running" % self.name)
#         time.sleep(2)
#         print("%s is done" % self.name)
#
#
# if __name__ == '__main__':
#     p = MyProcess("自定义类进程")
#     p.start()
#     print('master')

