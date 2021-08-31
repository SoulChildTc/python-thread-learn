from threading import Thread, Timer, current_thread, enumerate

"""
在指定的秒数后调用函数
"""


def hello():
    print("我是子线程%s我做我的事" % current_thread().getName())


t1 = Timer(5, hello)
t2 = Timer(2, hello)
t1.start()
t2.start()
# 启动线程后打印线程数量,可以看出并不是延迟启动线程,而是延迟启动函数
print("线程数量", len(enumerate()))

print("我是主线程%s，我做我的事" % current_thread().getName())
