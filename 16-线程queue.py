from threading import Thread, Timer, current_thread, enumerate
import queue

"""
使用基本同进程q
"""

q = queue.Queue(3)  # 队列：先进先出

q.put(1)
q.put(2)
q.put(3)
# q.put(4, block=False)

print(q.get())
print(q.get())
print(q.get())
######################################################
q = queue.LifoQueue(3)  # 堆栈，先进后出
q.put(1)
q.put(2)
q.put(3)
# q.put(4, block=False)

print(q.get())
print(q.get())
print(q.get())
######################################################

q = queue.PriorityQueue(4)  # 优先级队列
# 参数填写一个元组，元组中的第一个元素代表优先级,数值越小优先级越高
q.put((10, "a"))
q.put((0, 2))
q.put((-3, "1"))


print(q.get())
print(q.get())
print(q.get()[1])
