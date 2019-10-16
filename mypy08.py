# 函数（python 一切皆对象）一等对象
# def fn(a, b, c.txt):
#     print(a)
#     print(b)
#     print(c.txt)
#     print(a * b * c.txt)
#     return 'sss'
#
#
# # 位置参数放前面，关键字参数放后面
# # fn(1, c.txt=20, b=15)
#
# def fn2(a):
#     # 函数中对形参进行复制，不影响其他变量
#     # 形参是对象，会影响到所有指向该对象的变量
#     a = 50
#     print(a)
#
#
# # 实参可以传递任意类型的数据
# # fn2({'a': '123'})
# a = 10
# print(a)
# fn2(fn(1, c.txt=20, b=15))

# 装包（不定长参数）, *后面的参数必须以关键字形式传递 *参数只接受位置参数 **a 可接受关键字参数
# def fn(b, *a, c.txt, **d):
#     for i in a:
#         b += i
#     print(b + c.txt)
#     print(d)
#
#
# fn(10, 1, 2, 3, 4, c.txt=30, f=2, e=5, g=8)
# def fn4(a, b, c.txt):
#     print(a)
#     print(b)
#     print(c.txt)
#
#
# t = 10, 20, 30
# # 解包 自动将序列中的元素作为参数传递
# d = {'a': 100, 'b': 200, 'c.txt': 300}
# fn4(*t)
# fn4(**d)
#
#
# def fn5(a: int, b: bool, c.txt: str = 'hello') -> int:
#     """
#         这是一个打印 #文档字符串
#         # 返回值为int
#     """
#     print(1)
#
#
# print(help(fn5))

# 作用域和命名空间
# a = 20
#
#
# def fn():
#     global a
#     a = 10
#     print(a)
#
#
# fn()
# print(a)
#
#
# def fn2():
#     b = 30
#     # scope = locals()
#     scope = globals()
#     print('.' * 60)
#     print(scope)
#     # print(scope['b'])
#     print('.' * 60)
#
#     def fn3():
#         # b = 40
#         print(b)
#
#     fn3()
#
#     print(b)
#
#
# fn2()

# scope = locals()
# print(scope)
# print(scope['a'])

# 递归
# n = 10
# for i in range(1, 10):
#     n *= i
#
# print(n)
#
#
# def fn(f):
#     x = f
#     for m in range(1, f):
#         x *= m
#
#     return x
#
#
# print(fn(10))
#
#
# def fn2(h):
#     if h == 1:
#         return 1;
#     if h > 1:
#         return h * fn(h - 1)
#     else:
#         return False
#
#
# result = fn2(10)
# print(result)


# def power(m, i):
#     """
#     使用任意数字计算幂远算
#     :param m:
#     :param i:
#     :return: int
#     """
#     if i == 1:
#         return m
#     if i > 1:
#         return m * power(m, i - 1)
#     else:
#         return False
#
#
# print(power(10, 5))
# print(10 ** 5)
#
# my_str = 'abcdefggfedcba'
#
#
# # 回文 字符串从前往后和从后往前是一样的
# def words(new_str):
#     print(len(new_str))
#     if len(new_str) < 2:
#         return True
#     elif new_str[0] != new_str[-1]:
#         return False
#     else:
#         return words(new_str[1:-1])


# print(words('hell'))


# 高阶函数，接受一个或多个函数作为参数， 返回值为函数
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def fn(lst, func):
#     new_list = []
#     for i in lst:
#         if func(i):
#             new_list.append(i)
#
#     return new_list
#
#
# def fn2(i):
#     if i % 2 == 0:
#         return True
#     return False
#
#
# def fn3(i):
#     if i > 5:
#         return True
#     return False
#
#
# def fn4(i):
#     return i % 3 == 0


# print(fn(lst, fn4))
#
# print(filter(lambda a: a % 3, lst))
# r = map(lambda i: i ** 2, lst)
# print(list(r))

# 匿名函数 lambda 后面是参数 冒号后面试返回值
# f = lambda a, b, c.txt: a + b + c.txt
# print(f(1, 2, 3))
# print(type(f))

# l = ['bbb', 'cc', 'ffffff', 'ee', 11, 333]
# # l.sort(key=str or int)
#
# print(sorted(l,key=str,reverse=True))
#
# print(l)

# 闭包 通过闭包创建只能当前函数访问的变量
# 总是能访问到fn里面的变量
#
# def fn():
#     a = 20
#
#     def inner():
#         print('我是inner:a', a)
#
#     return inner
#
#
# r = fn()
# print(r)
#
# r()

# def aver():
#     nums = []
#
#     def inner(n):
#         nums.append(n)
#         return sum(nums) / len(nums)
#
#     return inner
#
#
# ave = aver()
# print(ave(10))
# print(ave(30))
# print(ave(10))
# print(ave(40))


# 装饰器 （对函数进行扩展，方便后期维护，不违反开闭原则）
def add(a, b):
    r = a + b
    return r


def mul(a, b):
    r = a * b
    return r


def fn():
    print('我是fn函数。。。。。。')


def fn2():
    print('函数开始执行')
    fn()
    print('函数执行结束')


fn2()


# def new_add(a, b, func):
#     print('函数开始执行')
#     r = func(a, b)
#     print('函数执行结束')
#
#     return r
#
#
# print(new_add(123, 456, add))
# print(new_add(123, 456, mul))

def began_end(func):  # 装饰器 可以在不修改原函数的情况下进行扩展
    def new_fun(*args, **kwargs):
        print('函数开始执行111')
        r = func(*args, **kwargs)
        print('函数执行结束22222')
        return r

    return new_fun


f = began_end(fn)

print(f())


@began_end  # @方法进行装饰 可以使用多个装饰器 函数将由内向外的顺序装饰
def say_hello():
    print('say hello')


say_hello()
