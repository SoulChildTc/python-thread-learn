from multiprocessing import Process
import os
import time


# join会阻塞后面的代码运行。确保子进程运行完毕，在运行主进程。
def task(n):
    print('%s is running' % os.getpid())
    # 获取父pid
    print('ppid is %s' % os.getppid())
    time.sleep(n)
    print('%s is done' % os.getpid())


if __name__ == '__main__':
    start_time = time.time()
    p1 = Process(target=task, name="task1", args=(3,))
    p2 = Process(target=task, args=(2,))
    p3 = Process(target=task, args=(1,))
    ############################################
    # # p1,p2,p3基本同时运行
    # p1.start()
    # p2.start()
    # p3.start()
    # # 先等p1执行完,在等p2执行,最后等p3
    # p1.join()
    # p2.join()
    # p3.join()
    ############################################
    # 用循环的方式
    p_l = [p1, p2, p3]
    for p in p_l:
        p.start()
    # 子进程是否存活
    print("子进程p1是否存活:", p1.is_alive())
    # 向操作系统发送信号，终止p3子进程
    p3.terminate()
    for p in p_l:
        print("等他运行完：----------", p)
        p.join()
    # 子进程是否存活
    print("子进程p1是否存活:", p1.is_alive())
    ############################################
    print('master', time.time() - start_time)
    print('master-pid', os.getpid())
    # 获取子进程名称
    print(p1.name)
