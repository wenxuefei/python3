# dict 属于映射
my_dict = {}
print(type(my_dict))
my_dict['name'] = 'wen'
my_dict['age'] = 18
my_dict = dict([('name', 'wen'), ('age', 18)])
my_dict = dict(name='wen', age=18)
print(len(my_dict))
print('name' in my_dict)
print('name' not in my_dict)
print(my_dict)

print(my_dict.get('name', '你好'))
print(my_dict.keys())
print(my_dict.items())
print(my_dict.values())
print(my_dict.setdefault('hell0', 'zhu'))  # key存在返回值，不存在，添加
my_dict1 = {'cc': 1000, 'dd': 22}
del my_dict1['cc']
print(my_dict.update(my_dict1))  # 合并字典
print(my_dict.pop('dd'))
print(my_dict.popitem())
print(my_dict.copy())  # 对象浅复制
# print(my_dict.clear())
print(my_dict)

# for i in my_dict:
#     print(my_dict[i])
#     print(i)
#     # print(v)

for k in my_dict.keys():
    print(k)

for v in my_dict.values():
    print(v)

for k, v in my_dict.items():
    print(k, '---------->', v)
