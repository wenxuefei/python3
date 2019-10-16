# python 的标准库 （开箱即用）
# pprint 可以用来对打印的数据进行格式化
import sys  # 系统模块 python解析器的信息
import pprint

# print(sys.argv)  # 获取执行代码时，命令中所包含的参数 返回值为列表
# pprint.pprint(sys.modules)  # 获取当前代码执行时，所引用的模块 返回值为字典
#
# # 模块的搜索路径
# pprint.pprint(sys.path)  #
#
# # 运行的平台
# pprint.pprint(sys.platform)  #
#
# # 方法
# sys.exit("程序出现异常")  # 退出程序
#
# print(123)

# 操作系统的模块
# import os
#
# # 获取到系统的环境变量
# pprint.pprint(os.environ['path'])  # 返回的对象不进行格式化
#
# # 可以用来执行操作系统的名字
# os.system('notepad')
# pprint.pprint(os)
