import re

# match 的使用
# s = 'hello world'
# pattern = 'Hello'
# o = re.match(pattern, s, flags=re.I)  # re.I 不区分大小写
# print(o)  # 未匹配返回None
# print(dir(0))
# print(o.group())  # 返回匹配的字符串
# print(o.span())   # 返回匹配的范围
# print(o.start())  # 返回匹配的开始字符索引

# 常用匹配符

# s = 'a'
# s = 'A'
# s = '8'
# s = '_'
# s = '\n'
#
# # pattern = '.'  # 除了\n 可匹配任意字符
# # pattern = '\d'  # 0 - 9 的数字
# # pattern = '\D'  # 非0 - 9 的数字
# # pattern = '\s'  # 空白 可以是 空格 \n \t
# # pattern = '\S'  # 非空白 可以是 空格 \n \t
# # pattern = '\w'    #   匹配字母，数字，下划线，
# # pattern = '\W'    #   匹配非字母，数字，下划线，
# o = re.match(pattern, s)
# print(o)

# 匹配列表
pattern = "[2468]"
s = "2"
o = re.match(pattern, s)
print(o)
