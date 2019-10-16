# 对象
# id 是有解析器生成的
# type 数据的类型
# a = 'hello'
# b = 1
# c.txt = 2
# d = []
# print(id(a))
# print(id(b))
# print(id(c.txt))
# print(type(d))


# 逻辑运算

# 逻辑非
e = True
e = not e
print(e)

# 逻辑与
result = True and True
result = True and False
print(result)

# 逻辑或
result2 = True or False
print(result2)

# 非布尔值逻辑运算
result3 = 1 and 2  # 若所有值均为真，则返回最后一个值，若存在假，返回第一个假值
result3 = 1 and 0
result3 = 0 and 1
print(result3)

result4 = 1 or 2  # 若第一个值为True，直接返回第一个
result4 = 1 or 0
result4 = 0 or 1
result4 = 0 or None
print(result4)

# 条件预算符（三元运算符）
a = 10
b = 20
c = 30
print("a的值比较大！") if a > b else print('b的值比较大！')
max1 = a if a > b else b
max1 = c if c > max1 else max1
max2 = a if (a > b and a > c) else (b if b > c else c)  # 不推荐
print(max1)
print(max2)
