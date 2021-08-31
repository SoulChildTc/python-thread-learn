from multiprocessing import Queue

q = Queue(3)

q.put('first')
q.put(2)
q.put({'count': 3})
# block=False不阻塞，如果队列满了，直接抛出异常
q.put("asd", block=False)  # 等价于q.put_nowait("asd")
# 超时时间,10s后如果 队列还是满的,就抛出异常
q.put("aa", timeout=10)

print(q.get())
print(q.get())
print(q.get())
# block=False不阻塞，如果队列是空的，直接抛出异常
print(q.get(block=False))  # 等价于q.get_nowait()
# 超时时间,10s后如果 队列还是空的,就抛出异常
q.get(timeout=10)
