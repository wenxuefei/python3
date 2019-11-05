# 模块 将一个完整的程序分解为一个个小的程序 通过将模块组合完成一个完整的程序
# 引用方式 1.import 2 import 。。。as 。。。 3 from 模块名 import 变量名 as 别名 4. from 模块名 import * （不推荐）
# import sys
# 添加了下划线的变量只能在模块中访问 通过import * 不会引用
import sys as s
# from sys import path
# print(s)
#
# # 检查模块是否为当前模块
# if __name__ == '__main__':
#     print(11111)
#     pass
#
# print(path)


# 包 （ package ）也是一个模块，是一个强大的模块
# 普通的模块就是一个文件 而包是一个文件夹
# 包中必须有一个 __init__.py 文件，这个文件可以包含有包中的主要内容
# 使用模块时也需要将模块（包）的代码转换为机器码然后再交由计算机执行
# 执行完后会有缓存代码，下次执行直接掉用缓存代码，来提升执行性能

# 包之间引用 . 表示当前目录  .. 表示上级目录

# from .hello import *

# import hello
# from hello import a
# print(a.a)
# print(hello.a)
# print(hello)

# sys.path 和 模块搜索路径
# import sys
# sys.path.append("E://") # 临时添加目录
# print(sys.path)

# 模块发布和安装
# 1.模块本地发布 发布 python setup.py sdist  安装 python setup.py install
# import my_package.demo1

# 2.远程发布
# (1) 注册PyPi官网
# (2) 创建用户信息文件 .pypirc
#       <1> 适用于Linux 输入并执行python setup.py register 然后输入用户名和密码
#       <2> 使用文件（适用于Windows和Linux）在用户的家目录创建一个文件为.pypirc：内容为
#            [distutils]
#            index-servers = pypi
#            [pypi]
#            repository =  http://upload.pypi.org/legacy/
#            username = 账户名
#            password = 密码

# 【注】
# （3）上传并发布 python setup.py sdist upload
#  (4) pip install my_package


