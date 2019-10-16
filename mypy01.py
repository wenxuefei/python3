# 字符串内容块

a = 'hello'
print('a = {0}'.format(a))
print(f'a = {a}')
print('a = %s%s' % ('你好', '中国'))
print(a.split('l', 1))
print(a[0::2])

if 'h' in a:
    print("h 在变量 a 中")

if 'm' not in a:
    print("m 不在变量 a 中")

name = 'hhh'

print('欢迎 ' + name + ' 光临！')
print('欢迎', name, '光临！')
print('欢迎%s光临！' % name)
print(f'欢迎{name}光临！')
print('欢迎{0}光临！'.format(name))

c = 'abc'
print(c * 3)
d = 123
print(type(a))
print(type(d))
