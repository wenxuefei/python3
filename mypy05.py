# tuple ( 元组 ) 不可变对象

my_tuple = tuple(range(10))
my_tuple = 1, 2, 3, 4, 5, 6

# 元组\列表\字符串都可以解包
a, b, c, d, e, f = my_tuple
a, b, c, *d = my_tuple  # 变量数量和元素数量一致，也可在变量前面添加*，返回列表
# 交换值
a, b = b, a

print(a)
print(b)
print(c)
print(d)
print(type(my_tuple))
print(my_tuple)


# == 比较的是对象的值是否相等  is 和 is not 比较的是对象是否相等