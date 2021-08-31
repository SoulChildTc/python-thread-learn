"""
迭代器：
可迭代对象：有__iter__方法
迭代器：有__iter__方法和__next__方法
iter方法可以将可迭代对象转换成迭代器
"""
import time

# # 自己实现一个可迭代对象
# class MyIter(object):
#     x = 0
#
#     def __iter__(self):
#         # 必须返回一个迭代器，self中包含__next__方法，所以MyIter是一个迭代器
#         return self
#
#     def __next__(self):
#         if self.x >= 10:
#             raise StopIteration
#         else:
#             self.x += 1
#             return self.x
#
#
# ml1 = MyIter()
#
# for i in ml1:
#     print(i)
#     time.sleep(1)

############################################################################
# 斐波那契数列
# 下面直接生成一个列表
# nums = []
# a = 0
# b = 1
# count = 0
# while count < 10:
#     nums.append(a)
#     a, b = b, a + b
#     count += 1
# print(nums)


# 用迭代器的方式
# class fbnq(object):
#     a = 0
#     b = 1
#     count = 0
#
#     def __init__(self, length):
#         self.length = length
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.length > self.count:
#             ret = self.a
#             self.a, self.b = self.b, self.a + self.b
#             self.count += 1
#             return ret
#         else:
#             # 抛出异常就代表没有值了,停止迭代
#             raise StopIteration
#
#
# # for循环，通过迭代器取出前10位斐波那契数列
# for i in fbnq(10):
#     print(i)
#
# # 转换列表，通过迭代器取出前5位斐波那契数列
# print(list(fbnq(5)))
############################################################################

"""
生成器就是迭代器
函数中包含yield,yield的结果就是生成器对象
"""


# # 生成器
# def create_num(length):
#     a, b = 0, 1
#     count = 0
#     while count < length:
#         yield a  # 每调用一次next方法会将代码执行到yield这个位置
#         a, b = a + b, a
#         count += 1
#     return None
#
#
# for i in create_num(10):
#     print(i)


# 使用生成器实现一个range功能
# def my_range(start, end, step=1):
#     while start < end:
#         yield start
#         start += step
#
#
# for i in my_range(1, 5):
#     print(i)


# 生成器写tail+grep命令
# def tail(filepath):
#     with open(filepath, 'rb') as f:
#         f.seek(0, 2)
#         while True:
#             line = f.readline()
#             if line:
#                 yield line
#             else:
#                 time.sleep(0.05)
#
#
# def grep(content_obj, pattern):
#     for line in content_obj:
#         line = line.decode('utf8')
#         if pattern in line:
#             yield line
#
#
# for i in grep(tail("tmp.txt"), "404"):
#     print(i)


# 表达式yield，可以传值

def eater(name):
    print("%s ready eat" % name)
    while True:
        # 提示: 先执行等号右边的内容(yield "收到"),执行后就停止了，然后下次运行(next)的时候才有赋值操作。
        food = yield "收到"
        print("%s 吃了 %s" % (name, food))


p = eater('xxx')
# 初始化
print(next(p))  # 执行到第一个yield，打印出收到
# send相当于先传值在next
print(p.send("一个苹果"))  # 接着上面执行,将一个苹果赋值给food,打印吃了一个苹果，再执行到yield "收到"，打印收到
print(p.send("一个西瓜"))  # 接着上面执行,将一个西瓜赋值给food,打印吃了一个西瓜，再执行到yield "收到"，打印收到
