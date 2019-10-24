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
# pattern = "[2468]"
# s = "2"
# o = re.match(pattern, s)
# print(o)

# 匹配手机号码
# pattern = '1[35789]\d\d\d\d\d\d\d\d\d'
# s = '13456789444'
# o = re.match(pattern, s)
# print(o)

# 符号使用
# pattern = '\d*'  # * 0次到多次
# pattern = '\d+'  # * 至少一次
# pattern = '\d?'  # * 0次或一次
# pattern = '\d{2}'  # * {m} : m次
# pattern = '\d{2,5}'  # * {m,n} : m-n次
# pattern = '\d{2,}'  # * {m,} : 至少m次
# s = '123qwe'
# o = re.match(pattern, s)
# print(o)

# 实例
# 匹配一个字符串首字母为大写，后面为小写， 小写可有可无
# pattern = '[A-Z][a-z]*'
# s = 'Hello'
# o = re.match(pattern, s)
# print(o)

# 匹配有效的变量名
# pattern = '[a-zA-Z_]\w*'
# s = '_'
# o = re.match(pattern, s)
# print(o)

# 匹配1-99 的数字
# pattern = '[1-9]\d?$'
# s = '999'
# o = re.match(pattern, s)
# print(o)

# 匹配随机密码
# pattern = '\w{8,20}'
# s = '12345678'
# s = '12345678#'
# o = re.match(pattern,s)
# print(o)

# 转义字符的使用
# s = '\\t123'
# pattern = r'\\t\d*'  # 原生字符串
# o = re.match(pattern, s)
# print(o)

# 边界字符
# 匹配qq邮箱
# q = '5589858@qq.com'
# pattern = '^[1-9]\d{4,9}@qq.com$'
# o = re.match(pattern,q)
# print(o)
# \b 单词边界
# pattern = r'.*\bab'  # 左边界
# pattern = r'.*ab\b'  # 有边界
# s = '123456 ab'
# o = re.match(pattern, s)
# print(o)
# \B 非单词边界
# pattern = r'.*\Bab'  # 左边界
# pattern = r'.*ab\B'  # 有边界
# s = '123456 abc'
# o = re.match(pattern, s)
# print(o)

# search 方法
# pattern = 'hello'
# s = 'hello python'
# m = re.search(pattern, s)
# print(m)

# 匹配多个字符
# pattern = 'aa|bb|cc'
# s = 'my name is bb'

# 匹配0 - 99|100 所有的数字
# pattern = '[1-9]?\d$|100$'
# s = '100'
# o = re.match(pattern, s)
# m = re.search(pattern, s)
# print(o)
# print(m)

# [] 和 | 相同及不同
# m = re.match(r'[xyz]', 'x')
# o = re.match(r'x|y|z', 'x')
# print(m)
# print(o)

# pattern = '[ab][cd]'
# pattern = 'ab[cd]'
# pattern = 'ab|cd'
# s = 'ac'
# s = 'ad'
# s = 'ab'
# s = 'abc'
# s = 'abd'
# print(re.match(pattern, s))

# 分组（）
# 匹配座机号码
# pattern = r'(\d{3,4})-([1-9]\d{4,7}$)'
# s = '010-7986545'
# o = re.match(pattern, s)
# print(o.groups()[0])
# print(o.groups()[1])
# print(o.group(1))
# print(o.group(2))

# 匹配网页标签
# s = '<html><head>head部分</head></html>'
# # s = '<html><title>>head部分</head></html>'
# # pattern = '<.+><.+</.+></.+>'
# # pattern = r'<(.+)><(.+)>.+</\2></\1>'
# pattern = r'<(?P<k_html>.+)><(?P<k_head>.+)>.+</(?P=k_head)></(?P=k_html)>'
# o = re.match(pattern, s)
# print(o)

# 其他方法
phone = '2004-959-559 # 这是一个国外电话'
# 删除字符串中的注释去掉
pattern = '#.*$'
pattern = r'\D'
res = re.sub(pattern, '', phone)
res = re.subn(pattern, '', phone)
print(res)

s = 'first123 line'
regex = re.compile(r'\w+')
print(regex)
o = regex.match(s)

s = 'first 1 second 2 third 3'
pattern = r'\w+'
o = re.findall(pattern, s)
o = re.finditer(pattern, s)
for i in o:
    print(i.group(), end='\t')
print(o)

pattern = r'\d+'
result = re.split(pattern, s)
print(result)
result = re.split(pattern, s, maxsplit=2)
print(result)

v = re.match(r'(.+)(\d+-\d+-\d+)', 'This is my tel:133-1234-1234')
print('----------贪婪模式---------')
print(v.group(1))
print(v.group(2))
print('----------非贪婪模式---------')
v = re.match(r'(.+?)(\d+-\d+-\d+)', 'This is my tel:133-1234-1234')
print(v.group(1))
print(v.group(2))
print('-------实例2--------')
print('贪婪模式')
v = re.match(r'abc(\d+)', 'abc123')
print(v.group(1))  # 123
# 非贪婪模式
print('非贪婪模式')
v = re.match(r'abc(\d+?)', 'abc123')
print(v.group(1))  # 1
