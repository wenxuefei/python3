# list 可变序列
my_list = list(range(10))  # 构造器创建列表
# print(my_list[-2])
# print(my_list)
# # for i in my_list:
# #     print(my_list[i])
#
# # list slice 不影响原来列表，返回新列表
# print(my_list[:])
# print(my_list[3:])
# print(my_list[::2])
# print(my_list[::-1])  # 相当于list倒叙
# print(my_list[:5])
# print(my_list[:5:2])  # 第一个参数为起始位置，第二个为结束位置，第三个为step（步长,步长不可为0）

# 拼接和重复
my_list1 = list(range(20, 30)) * 2
# print(my_list + my_list1)
# print(my_list1 * 2)

# in 和 not in
# print(20 in my_list1)
# print(100 not in my_list1)

# 长度 len 最小值 min 最大值 max
# print(len(my_list1))
# print(min(my_list1))
# print(max(my_list1))

# 方法
print(my_list1.index(20, 3))  # 获取指定元素的位置（第一次出现）第二个参数为查找的起始位置，第三个为结束位置
print(my_list1.count(20))  # 获取制定元素个数

# 修改列表(只适用于可变序列)

# 索引修改列表
del my_list1[0]  # 删除元素（根据元素）
my_list1[1] = 30
my_list1[0:2] = [1, 2, 3]  # 替换
my_list1[0:0] = [10]  # 插入元素
my_list1[0::10] = [500, 700, 800]
my_list1[1:3] = []

# 方法修改列表
my_list1.reverse()  # 列表倒叙
my_list1.append(10000)  # 添加元素(列表最后)
my_list1.remove(28)  # 移除指定元素(根据值) 删除第一个
my_list1.insert(2, 20000)  # 插入元素
my_list1.extend([5, 6, 7])  # 添加列表
print(my_list1.pop(1))  # 根据索引删除元素
# my_list1.clear()  # 清空列表
print(my_list1.copy())  # 列表拷贝
print(my_list1.sort(reverse=True))  # 根据值排序（默认升序）reverse = True 降序

print(my_list1)
