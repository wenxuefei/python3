# set (集合) 只能存储不可变对象 是无序的,不可重复
s = {1, 2, 3, 4}
s = {10, 1, 2, 5, 12}
s = set()
s = set({1, 2, 3, 4, 5})
s = set([1, 2, 3, 4, 5])
s = set('hello')
# 添加
s.add(10)
s.update((20, 30, 40, 59))

# 删除
print(s.pop())
print(s.remove(20))

print(s.copy())

s1 = set('hello')
s1.add(4)
# 交集
print(s & s1)

# 并集
print(s | s1)
# 差集
print(s - s1)
print(s.difference(s1))
# 异或集 (不想交的元素)
print(s ^ s1)
# 是否为子集
s2 = {40, 10, 59}
print(s <= s1)
print(s2 <= s)
# 是否为真子集
print(s2 < s)
print({1, 2, 3} < {1, 2, 3})
# print(s.clear())
# s = set({'a': 1, 'b': 2})
# print('a' in s)
# print('a' not in s)
# print(len(s))
print(s)
print(type(s))
