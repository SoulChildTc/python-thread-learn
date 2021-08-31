import time
import random
from multiprocessing import Queue, Process, JoinableQueue


# def producer(name, food, q):
#     for i in range(3):
#         res = '%s%s' % (food, i)
#         time.sleep(random.randint(1, 3))
#         print('厨师[%s]生产了-%s' % (name, res))
#         q.put(res)
#
#
# def consumer(name, q):
#     while True:
#         res = q.get()
#         if not res:
#             print("造完了,也吃完了")
#             break
#         time.sleep(random.randint(1, 3))
#         print('客人[%s]吃了-%s' % (name, res))
#
#
# if __name__ == '__main__':
#     q = Queue()
#     # 生产者
#     p1 = Process(target=producer, args=("王麻子", "面条", q))
#     p2 = Process(target=producer, args=("soulchild", "泔水", q))
#
#     # 消费者
#     c1 = Process(target=consumer, args=("sb", q))
#     c2 = Process(target=consumer, args=("sb2", q))
#
#     p1.start()
#     p2.start()
#     c1.start()
#     c2.start()
#     p1.join()
#     p2.join()
#     q.put(None)
#     q.put(None)
#     print('主')


# 使用JoinableQueue+daemon进程,对上面的代码进行改造


def producer(name, food, q):
    for i in range(3):
        res = '%s%s' % (food, i)
        time.sleep(random.randint(1, 3))
        print('厨师[%s]生产了-%s' % (name, res))
        q.put(res)


def consumer(name, q):
    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print('客人[%s]吃了-%s' % (name, res))
        # 确认消费完成
        q.task_done()


if __name__ == '__main__':
    q = JoinableQueue()
    # 生产者
    p1 = Process(target=producer, args=("王麻子", "面条", q))
    p2 = Process(target=producer, args=("soulchild", "泔水", q))

    # 消费者
    c1 = Process(target=consumer, args=("sb", q))
    c2 = Process(target=consumer, args=("sb2", q))
    c1.daemon = True
    c2.daemon = True
    p1.start()
    p2.start()
    c1.start()
    c2.start()
    # 等待生产者完成生产
    p1.join()
    p2.join()
    # 当队列中所有消息都被消费后就会停止阻塞。与消费者的q.task_done()配合使用
    q.join()
    print('主')
