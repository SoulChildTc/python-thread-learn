from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from threading import current_thread
import time
import random
import os

"""
提交任务的两种方式:
同步调用:提交完任务后，就在原地等待，等待任务执行完毕，拿到任务的返回值，才能继续执行下一行代码,导致串行
异步调用:提交完任务后，不再原地等待，并发执行。一般和回调配合使用

进程的执行状态:
阻塞: IO
非阻塞: IO
"""

###########################################################################
# 进程池
# def task(n):
#     print("%s is running" % os.getpid())
#     time.sleep(1)
#     return n ** 2
#
#
# def handle(res):
#     print(res.result())
#
#
# if __name__ == '__main__':
#     # 创建进程池，指定大小
#     pool = ProcessPoolExecutor(4)
#
#     for i in range(5):
#         # 异步提交任务
#         obj = pool.submit(task, i)
#         # 将执行结果传给回调函数handle
#         obj.add_done_callback(handle)
#         # 同步提交任务
#         # print(pool.submit(task, i).result())
#     # 等待进程池所有进程运行完毕，然后关闭进程池，不再接收新的提交任务
#     pool.shutdown(wait=True)
#     print("主")


###########################################################################
# 线程池
import requests


def get(url):
    print("%s 下载%s:" % (current_thread().getName(), url))
    time.sleep(2)
    response = requests.get(url)
    if response.status_code == 200:
        return {"url": url, "content": response.text}


def parse(res):
    res = res.result()
    print('parse:[%s] res:[%s]' % (res['url'], len(res['content'])))


if __name__ == '__main__':
    pool = ThreadPoolExecutor(2)
    urls = [
        "https://www.baidu.com",
        'https://soulchild.cn',
        'https://python.org',
        'https://soulchild.cn',
        'https://soulchild.cn',
        'https://soulchild.cn',
        'https://soulchild.cn',
        'https://soulchild.cn',
    ]
    for url in urls:
        # 提交任务到线程池
        pool.submit(get, url).add_done_callback(parse)
