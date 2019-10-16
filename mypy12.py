# 异常

# try:
#     print(10 / 0)
# except BaseException as e:
#     print(e)
# finally:
#     print('程序继续执行')
#
# print(123)


# 自定义异常
# class MyError(Exception):
#     pass
#
# def add(a, b):
#     if a < 0 or b < 0:
#         # raise Exception('两个参数中不可以有负数')
#         raise MyError('自定义异常')
#         # return None
#     r = a + b
#     return r
#
#
# print(add(-2, 456))

# 文件操作
# IO ( input/output ) 读写文件
# 写
# f = open('a.txt', 'w')
# f.write('123')
# f.close()

# 读
# f = open(r'a.txt', 'r')
# print(f)
# f.close()

# try:
#     with open(r'a.txt', 'r', encoding='utf-8') as f:
#         # f.read() # 读取全部内容 文件太大 容易导致内存泄漏 不建议直接调用read
#         print(f.read(1))  # 读取字符的数量 读取到文件最后会返回空字符穿
#         print(f.readline())  # 读取一整行
#
# except FileNotFoundError:
#     print('a.txt文件不存在')


# 读取大文件
# try:
#     with open(r'a.txt', 'r', encoding='utf-8') as f:
#         # 定义一个变量 循环读取文件内容
#         chunk = 100
#         # print(f.readlines())  # 读取所有行 返回列表
#         # for t in f:
#         #     print(t)
#         while True:
#             content = f.read(chunk)
#             if not content:
#                 print('内容读取完毕', end='')
#                 break
#             print(content)
#
#
# except FileNotFoundError:
#     print('a.txt文件不存在')

# 写入大文件 w 对原有的内容进行覆盖  a 追加内容 r+ w+ （可读可写 文件不存在会报错） x 新建文件 不存在创建
# try:
#     with open(r'a.txt', 'a', encoding='utf-8') as f:
#         # f.write('6666\n7777777777\n') # 返回值为字符串长度
#         f.writelines('444\n')
#         f.writelines('555\n')
#
#
# except FileNotFoundError:
#     print('a.txt文件不存在')

# 二进制文件 rb 读  wb 写 ab 追加

# try:
#     with open(r'表态.krc', 'rb') as f:
#         # f.write('6666\n7777777777\n') # 返回值为字符串长度
#         # print(f.read())
#
#         with open(r'表态01.krc', 'wb') as f2:
#             chunk = 1024 * 1
#
#             while True:
#                 content = f.read(chunk)
#                 # 修改读取的位置
#                 # f.seek(55) 第一个切换到的位置 第二个计算方式 0 从头计算 1 从当前位置计算 2 从最后位置开始计算
#                 # break
#                 print('当前读取到了--》', f.tell())  # 读取到了的位置
#
#                 if not content:
#                     break
#
#                 f2.write(content)
#
#
#
# except FileNotFoundError:
#     print('a.txt文件不存在')

# os 模块
import os
from pprint import pprint

# r = os.listdir()  # 查看指定目录的所有文件
# os.getcwd()  # 获取当前所在的目录
# os.chdir('..')  # 切换目录
# os.mkdir('aa', '777')  # 创建目录
# os.rmdir('aa')  # 删除目录
# os.rename('a.txt', 'bb.txt')  # 重命名
# os.rename('bb.txt', 'c.txt://bb.txt')  # 截切文件
# pprint(r)

# 获取文件和文件夹相关信息
# print(os.name)  # 返回操作系统
# print(os.sep)  # 返回系统分隔符
# print(repr(os.linesep))  # 返回系统换行符
# print(os.stat('mypy02.py'))  # 返回文件信息
# print(os.getcwd())  # 获取当前所在的目录 工作目录（空间）

# os.chdir("d:")  # 切换工作目录

# 目录创建
# os.mkdir("aa")  # 创建单个目录
# os.rmdir("aa")  # 移除目录
# os.makedirs("电影/港台/周星驰/功夫.MP4")  # 创建多级目录
# os.removedirs("电影/港台/周星驰/功夫.MP4")  # 删除多级目录 (只能删除空目录)

# os.rename("电影", "movie")  # 重命名
# print(os.listdir("movie"))

# os.path 模块
import os
from os import path

#  文件，目录，绝对路径，文件是否存在 判断
# print(path.isabs("e:/a.txt"))
# print(path.isdir("e:/a.txt"))
# print(path.isfile("d:/a.txt"))
# print(path.exists("e:/a.txt"))

# 获取文件基本信息
# print(path.getsize("a.txt"))
# print(path.abspath("a.txt"))
# print(path.dirname(r"E:\python\a.txt"))
#
# # 获取文件时间信息
# print(path.getctime("a.txt"))  # 创建时间
# print(path.getatime("a.txt"))  # 访问时间
# print(path.getmtime("a.txt"))  # 修改时间
#
# # 对路径的操作
# path2 = path.abspath("a.txt")
# print(path.split(path2))  # 分割路径
# print(path.splitext(path2))  # 获取文件扩展名
# print(path.join("aa", "bb", "cc"))  # 路径连接
#
# list1 = os.listdir()
# for i in list1:
#     # if i.endswith('py'):
#     #     print(i)
#     if path.splitext(i)[1] == '.py':
#         print(i)
#
# print('------------------------------------------')
# list2 = [filename for filename in os.listdir() if filename.endswith('py')]  # 推导式生成
#
# for i in list2:
#     print(i)

# walk 递归遍历子目录和子文件
# import os
# all_files = []
# path1 = os.getcwd()
# list1 = os.walk(path1)
# for dirpath, dirnames, filenames in list1:
#     for dir in dirnames:
#         all_files.append(os.path.join(dirpath,dir))
#         # print(dir)
#         # print(os.path.join(dirpath,dir))
#     for file in filenames:
#         all_files.append(os.path.join(dirpath, file))
#         # print(file)
#     # for p in dirpath:
#     #     print(p)
#
# for file in all_files:
#     print(file)


# shutil 模块拷贝和压缩
import shutil

# shutil.copyfile("a.txt", "b.txt")  # 文件拷贝
# shutil.copytree("movie/港台", "电影")  # 目录拷贝 文件已存在时，无法拷贝
# shutil.copytree("movie/港台", "电影", ignore=shutil.ignore_patterns("*.txt", "8.html"))  # 目录拷贝 文件已存在时，无法拷贝

# zip 压缩，解压缩
# shutil.make_archive("电影/gg", "zip", "movie/港台")  # 第一个为压缩后的路径，名称 第二个为压缩形式 第三个压缩内容
# import zipfile  # 压缩文件

# z1 = zipfile.ZipFile("a.zip", "w")
# z1.write("a.txt")
# z1.write("b.txt")
# z1.close()
# 解压缩文件
# z2 = zipfile.ZipFile("a.zip", "r")
# z2.extractall("电影")
# z2.close()

# 递归打印所有的目录和文件
# import os
#
# allFIles = []
#
#
# def getAllFiles(path, level):
#     child = os.listdir(path)
#     for file in child:
#         filePath = os.path.join(path, file)
#
#         # print("\t" * level + filePath)
#
#         if os.path.isdir(filePath):
#             getAllFiles(filePath, level + 1)
#
#         # allFIles.append("\t" * level + filePath)
#
#
# getAllFiles("movie", 0)
# for i in reversed(allFIles):
#     print(i)
