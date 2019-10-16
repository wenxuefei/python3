import numpy as np
import math

# 创建一个数组
# a = np.arange(10)
# print(a)
# print(type(a))
#
# # 对 ndarray 对象类型进行向量处理
# print(np.sqrt(a))
#
# # 对列表中的元素开平方
# b = [3, 4, 9]
# result = []
# for i in b:
#     print(math.sqrt(i))
#     result.append(math.sqrt(i))
# print(result)

# # 使用array创建一维数组
# a = np.array([1, 2, 3, 4])
# print(a)
# print(type(a))
#
# # 使用array创建二维数组
# b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(b)
# print(type(b))
#
# # 使用array创建三维数组
# c = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
# print(c)
# print(type(c))
#
# # dtype元素的类型
# d = np.array([3, 4, 5], dtype=float)
# print(d)
#
# # ndmin维度
# e = np.array([5, 6, 7], dtype=float, ndmin=3)
# print(e)

# # arange 创建（1-10）数组 第一个为开始，第二个为结束（不包含结束值）第三个为步长
# a = np.arange(1, 11, 2, dtype=float)
# print(a)

# # random 创建随机一维数组(0.0,1.0)
# a = np.random.random(size=5)
# print(a)

# # random 创建随机二维数组
# b = np.random.random(size=(3, 4))
# print(b)

# # random 创建随机三维数组
# c = np.random.random(size=(2, 3, 4))
# print(c)

# 随机整数 一维数组（0，5）第一个为起始值，第二个为结束值，size为个数
# a = np.random.randint(5, size=10)
# print(a)

# # 随机整数 二维数组（0，5）第一个为起始值，第二个为结束值，size为个数
# a = np.random.randint(5, 10, size=(3, 4))
# print(a)

# # 随机整数 三维数组（0，5）第一个为起始值，第二个为结束值，size为个数 dtype 为int 和 int64默认int
# a = np.random.randint(5, 10, size=(2, 3, 4), dtype=np.int64)
# print(a)
# print('a的类型', a.dtype)

# # 创建一维
# a = np.random.randn(4)
# print(a)
#
# # 创建二维
# b = np.random.randn(2, 3)
# print(b)

# # 创建三维
# b = np.random.randn(2, 3, 4)
# print(b)

# # 创建指定期望和方差的正太分布
# a = np.random.normal(size=5)  # 默认的期望是loc=0.0 方差scale=1.0
# print(a)
# b = np.random.normal(loc=2, scale=5, size=(3, 4))
# print(b)

# a = np.array([1, 3, 4, 5])
# b = np.random.randint(4, 10, size=(3, 6))
# c = np.random.randn(2, 3, 4)
# print(a)
# print(b)
# print(c)
# # 元素维度
# print(a.ndim, b.ndim, c.ndim)
# # 元素形状
# print(a.shape, b.shape, c.shape)
# # 元素类型
# print(a.dtype, b.dtype, c.dtype)
# # 元素个数
# print(a.size, b.size, c.size)
#
# # 每个元素大小以字节为单位
# print(a.itemsize, b.itemsize, c.itemsize)

# # zeros 创建一维数组
# a = np.zeros((5,),dtype=int)
# print(a)
# print(a.shape)

# zeros 创建二维数组
# a = np.zeros((3,4),dtype=int)
# # print(a)
# # print(a.shape)

# # ones 创建数组
# a = np.ones(10)
# print(a)
# b = np.ones((2,5),dtype=int)
# print(b)

# empty 值为未知
# a = np.empty(8)
# print(a)
# b = np.empty((2, 3), dtype=int)
# print(b)

# 等差数列 第一个开始值，第二个结束值，第三个为生成个数
# a = np.linspace(5, 20, 5, endpoint=False)
# print(a)

# 等比数列
# a = np.logspace(5, 20, 10, endpoint=True)
# print(a)

# 一位数组的切片和索引 第一个起始值，第二个结束值，第三个步长[start:stop:step]
# a = np.arange(10)
# print(a[2:8:3])
# print(a[5])
# print(a[-3])

# # 二维数组的切片和索引
# a = np.arange(1, 13)
# # 对一位数组进行修改形状
# a = a.reshape((4, 3))
# print(a)
# # 索引的使用
# # 获取第三行
# print(a[2])
# # 获取第二行第三列
# print(a[1][2])
#
# # 切片的使用 【行进行切片,列的切片】【start:stop:step，start:stop:step】
# # 获取所有行和所有列
# print(a[:, :])
# # 获取所有行，部分列
# print(a[:, 1])
# # 获取所有行，第一，第二列
# print(a[:, 0:2])
#
# # 获取部分行，所有列 奇数行所有列
# print(a[::2, :])
#
# # 获取部分行，所有列 奇数行 第一，第二列
# print(a[::2, 0:2])

# # 使用坐标获取数组 [行，列]
# a = np.arange(1, 13)
# # 对一位数组进行修改形状
# a = a.reshape((4, 3))
#
# # 获取第二行第三列的元素
# print(a[1][2])
# print(a[1, 2])
#
# # 同时获取不同行不同列 获取第二行第三列 第三行第一列
# print(a[1, 2], a[2, 0])
# print(np.array([a[1, 2], a[2, 0]]))
#
# # 使用坐标
# print(a[(1, 2), (2, 0)])
#
# # 使用负数索引
# print('最后一行',a[-1])
# # 行倒叙
# print(a[::-1])
# # 行列都进行倒叙
# print(a[::-1,::-1])

# # 数组的复制
# a = np.arange(1, 13)
# a = a.reshape((3, 4))
# print(a)
#
# # b = np.copy(a)
#
# # a 进行切片处理 获取1,2行 1,2列
# # sub_a = b[:2, :2]
# # print(sub_a)
#
# # 对sub_a中第一行，第一列进行修改
# sub_aa = np.copy(a[:2, :2])
# sub_aa[0][0] = 100
# print(sub_aa)
# print(a)

# # 改变数组的维度
# # reshape 将一位数组改为二维，三维数组
# a = np.arange(1, 25)
# print(a)
#
# # 1改2 可以传输2,6 可以(2,6)
# b = a.reshape(2, 12)
# print(b)
#
# # 1改3 可以传输2,3,4 可以(2,3,4)
# c = a.reshape(2, 3, 4)
# print(c)
#
# # 通过np.reshape修改
# d = np.reshape(a, (2, 3, 4))
# print(d)
#
# # 将多维数组改为一位数组
# e = d.reshape(24)
# e = d.reshape(-1)
# e = d.ravel()
# e = d.flatten()
# print(e)

# 数组的拼接
# 水平方向拼接
# a = np.arange(1, 6)
# a = a.reshape((2, 2))
# print(a)
# b = np.arange(6, 10)
# b = b.reshape((2, 2))
# print(b)
# c = np.hstack((a, b))
# print(c)
#
# # 垂直方向拼接
# d = np.vstack((a, b))
# print(d)
#
# # axis 0 垂直 1水平 默认0
# e = np.concatenate((a, b), axis=0)
# print(e)
# f = np.concatenate((a, b), axis=1)
# print(f)

# 三维合并
# a = np.arange(1, 13).reshape(1, 2, 6)
# b = np.arange(101, 113).reshape(1, 2, 6)
# print(a)
# print(b)
# c = np.concatenate((a, b), axis=2)
# c = np.concatenate((a, b), axis=0)
# c = np.concatenate((a, b), axis=1)
# print(c)

# 数组分割
# x = np.arange(1, 9)
# # a = np.split(x, 4) # 平均分割
# a = np.split(x, [3, 5, 7])  # 按位置分割
# print(a)

# 二维数组分割
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

# 垂直方向分割
# b, c = np.split(a, 2, axis=0)  # 平均分割
# print(b)
# print(c)
# b, c, d = np.split(a, [2, 3], axis=0)  # 位置分割
# print(b)
# print(c)
# print(d)

# 水平分割
# b, c = np.split(a, 2, axis=1)  # 平均分割
# print(b)
# print(c)
# b, c, d = np.split(a, [2, 3], axis=1)  # 位置分割
# print(b)
# print(c)
# print(d)
# b, c = np.hsplit(a, 2) 水平分割
# print(b)
# print(c)
# b, c = np.vsplit(a, 2)  # 垂直分割
# print(b)
# print(c)

# 数组转置
a = np.arange(1, 25).reshape(2, 12)
# print(a)
# b = a.transpose()
# b = a.T
# b = np.transpose(a)
# print(b)

# 多维数组转置
# a = a.reshape(2, 3, 4)
# print(a)
# # b = np.transpose(a)
# # print(b)
# b = np.transpose(a, (1, 2, 0))  # (1,2,0) 为三个维度 转换后的维度（3，4，2）
# print(b)

# 数组算术
# a = np.arange(9).reshape(3, 3)
# b = np.array([10, 10, 10])
# print(a + b)
# # print(np.add(a, b))
# print(a - b)
# print(np.subtract(b, a))
#
# y = np.empty((3, 3),dtype=np.int)
# d = np.multiply(a, 10, out=y)
# print(y)

# 三角函数
# a = np.array([0, 30, 60, 90])
# print(np.sin(a))

# around ceil floor 四舍五入
a = np.array([1.0, 4.55, 123, 0.567, 25.332])
# print(np.around(a))
# print(np.ceil(a))
# print(np.floor(a))

# 聚合函数
# print(np.sum(a))
# a = np.arange(1, 13).reshape(3, 4)
# print(a)
# print(np.power(a, 2))
# x = np.arange(5)
# y = np.zeros(10)
# print(np.power(2, x, out=y[:5]))
# print(y)


# a = np.array([4, 3, 2, 5, 2, 1])
# print(np.median(a))

# 二维数组

# a = np.arange(1, 13).reshape(3, 4)
# print(a)
# print("垂直方向", np.median(a, axis=0))
# print("水平方向", np.median(a, axis=1))

# 平均值
# a = np.array([4, 3, 2, 5, 2])
# print(np.mean(a))
# a = np.arange(1, 13).reshape(3, 4)
# print(a)
# print("垂直方向", np.mean(a, axis=0))
# print("水平方向", np.mean(a, axis=1))
#
# print('sum', np.sum(a))
# print('max', np.max(a))
# print('min', np.min(a))
#
# # argmin argmax 最小值，最大值坐标
# print('argmin', np.argmin(a))
# print('argmax', np.argmax(a))
