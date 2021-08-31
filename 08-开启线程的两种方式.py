"""
1.多个线程共享一个进程的数据
2.创建线程的开销远远小于进程
"""
from threading import Thread
import time
import random


# 方式1
# def piao(name):
#     print('%s is piaoing' % name)
#     time.sleep(random.randint(1, 3))
#     print('%s is piao end' % name)
#
#
# if __name__ == '__main__':
#     t1 = Thread(target=piao, args=("alex",))
#     t2 = Thread(target=piao, args=("peiqi",))
#     t1.start()
#     t2.start()
#     print('主')


# 方式2
# class Mythread(Thread):
#     def __init__(self, name):
#         super(Mythread, self).__init__()
#         self.name = name
#
#     def piao(self):
#         print('%s is piaoing' % self.name)
#         time.sleep(random.randint(1, 3))
#         print('%s is piao end' % self.name)
#
#     def run(self):
#         self.piao()
#
#
# t1 = Mythread("aql")
# t2 = Mythread("alex")
# t1.start()
# t2.start()
# # join会阻塞后面的代码运行。确保子进程运行完毕，在运行主进程。
# t1.join()
# t2.join()
# print("master")

#################################################################
# 获取线程的返回值
# class Mythread(Thread):
#     def __init__(self, name):
#         super(Mythread, self).__init__()
#         self.name = name
#         self.res = None
#
#     def piao(self):
#         print('%s is piaoing' % self.name)
#         time.sleep(random.randint(1, 3))
#         print('%s is piao end' % self.name)
#         return 1
#
#     def run(self):
#         self.res = self.piao()
#
#
# t1 = Mythread("aql")
# t2 = Mythread("alex")
# t1.start()
# t2.start()
# # join会阻塞后面的代码运行。确保子进程运行完毕，在运行主进程。
# t1.join()
# t2.join()
# print("master")
# print(t1.res)
# print(t2.res)
