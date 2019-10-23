"""
    高阶函数：将函数作为一个函数的参数
    函数式编程： 高度抽象的编程范式
"""

# def add(x, y, f):
#     return f(x) + f(y)
#
#
# print(add(-10, 5, abs))

# 内置高阶函数
# map 的使用
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = [11, 12, 13]
#
#
# def f(x):
#     return x * x
#
#
# resList = []
#
# for i in a:
#     resList.append(f(i))
#
# print(resList)
#
# it = list(map(f, a))  # 第一个为操作函数，第二个为操作数据 返回的是map可迭代对象
# print(it)
# # from collections import Iterator
# #
# # print("判断是否为可迭代对象", isinstance(it, Iterator))
# # print(list(it))
#
# # 将数字转换为字符串
# print(list(map(str, a)))
#
#
# def f1(x, y):
#     return x + y
#
#
# # 传输多个参数
# print(list(map(f1, a, b)))

# reduce的使用
# from functools import reduce
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num = 0
# for i in a:
#     num += i
# print(num)
#
#
# def sumTest(x, y):
#     return x + y
#
#
# print(reduce(sumTest, a))
# print(reduce(lambda x, y: x + y, a))

# filter的使用
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = ['A', '', 'B', None, 'C', ' ']
#
#
# def is_odd(n):
#     return n % 2 == 1
#
#
# def not_empty(n):
#     return n and n.strip()
#
#
# print(list(filter(not_empty, b)))
# print(list(filter(is_odd, a)))

# sorted 的使用 默认升序 倒叙reverse=True key 接收函数，表示排序方式
# sort_list = sorted([42, 422, 4, 2, -100, 3, -10], reverse=True)
# print(sort_list)
#
# sort_list = sorted(['abc', 'ABC', 'D', 'd', 'c'])
# print(sort_list)
#
# sort_list = sorted([42, 422, 4, 2, -100, 3, -10], key=abs)
# print(sort_list)
#
# sort_list = sorted(['abc', 'ABC', 'D', 'd', 'c'], reverse=True, key=str.lower)
# print(sort_list)

# 匿名函数
# f = lambda a, b, c: a + b + c
# print(f(2, 3, 4))

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# stu1 = Student("zhangsan", 21)
# stu2 = Student("lisi", 25)
# stu3 = Student("wangwu", 23)
#
# resList = sorted([stu1, stu2, stu3], key=lambda x: x.age)
# resList = sorted([stu1, stu2, stu3], key=lambda x: x.name, reverse=True)
# for stu in resList:
#     print('name:', stu.name, 'age:', stu.age)


# 闭包
# def out(num1):
#     def funIn(num2):
#         return num1 + num2
#
#     return funIn
#
#
# f = out(100)
# result = f(200)
# print(result)

# 闭包实现两点之间的距离
# import math
#
#
# def getDistance(x1, y1, x2, y2):
#     return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#
#
# # 求点（1,1）（0,0）的距离
# print(getDistance(1, 1, 0, 0))
#
#
# def getDisOut(x1, y1):
#     def getDisIn(x2, y2):
#         return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
#
#     return getDisIn
#
#
# f = getDisOut(1, 1)
# res = f(0, 0)
# print(res)

# 闭包的特殊用法
# import time
#
#
# def fun1():
#     # write_log(fun1)
#     print('功能1')
#
#
# def fun2():
#     # write_log(fun2)
#     print('功能2')
#
#
# def write_log(func):
#     try:
#         file = open('writeLog.txt', 'a', encoding='utf-8')
#         file.write('访问：' + func.__name__)
#         file.write('\t')
#         file.write("时间：" + time.asctime())
#         file.write('\n\n')
#     except Exception as e:
#         print(e)
#     finally:
#         file.close()
#
#
# def funcOut(func):
#     def funcIn():
#         write_log(func)
#         func()
#
#     return funcIn
#
#
# fun1 = funcOut(fun1)
# fun1()
# fun2 = funcOut(fun2)
# fun2()
# fun1()
# fun2()

# 装饰器

# import time
#
# def write_log(func):
#     try:
#         file = open('writeLog.txt', 'a', encoding='utf-8')
#         file.write('访问：' + func.__name__)
#         file.write('\t')
#         file.write("时间：" + time.asctime())
#         file.write('\n\n')
#     except Exception as e:
#         print(e)
#     finally:
#         file.close()
#
#
# def funcOut(func):
#     def funcIn():
#         write_log(func)
#         func()
#
#     return funcIn
#
#
# @funcOut
# def fun1():
#     print('功能1')
#
#
# @funcOut
# def fun2():
#     print('功能2')
#
# fun1()
# fun2()

# 装饰器练习(多个装饰器)
# def funOut(func):
#     print('装饰器')
#
#     def funIn():
#         print('I am foo')
#         func()
#
#     return funIn
#
# def funOut2(func):
#     print('装饰器2')
#
#     def funIn():
#         print('hello')
#         func()
#
#     return funIn
#
# @funOut2
# @funOut
# def foo():
#     print('foo函数正在运行')
#
#
# foo()

# 带参数的装饰器
# import time
#
#
# def write_log(func):
#     print('访问：', func.__name__, '\t时间：', time.asctime())
#
#
# def funcOut(func):
#     def funcIn(*args, **kwargs):
#         write_log(func)
#         return func(*args, **kwargs)
#
#     return funcIn
#
#
# @funcOut
# def sum(a, b):
#     return a + b
#
#
# @funcOut
# def add(a, b, c):
#     return a + b + c
#
#
# print(sum(10, 20))
# print(add(10, 20, 30))


# 偏函数
print(int('123456'))
print(int('123456', base=8))  # 转化为8进制
print(int('123456', base=16))  # 转化为16进制
print(int('10101010', base=2))  # 转化为2进制

from functools import partial

new_int = partial(int, base=2)
print(new_int('1010'))
