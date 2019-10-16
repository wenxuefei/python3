# 水仙花数 循环语句及控制语句
# i = 100
# while i < 1000:
#     # 判断i是否为水仙花数
#     a = i // 100  # 百位数
#     # b = i // 10 % 10 # 十位数
#     b = (i - a * 100) // 10  # 十位数
#     c.txt = i % 10
#     # print(b)
#     if i == a ** 3 + b ** 3 + c.txt ** 3:
#         print(i)
#     i += 1

# 判断是否为质数
# num = int(input("请输入任意大于一的整数"))
# # flag = False
# # i = 2
# # while i < num:
# #     if num % i == 0:
# #         flag = True
# #         break
# #     i += 1
# #
# # if flag:
# #     print("{0}是合数".format(num))
# # else:
# #     print("{0}是质数".format(num))


# 打印*
# i = 0
# while i < 10:
#     j = 0
#     while j < i:
#         print('*', end=' ')
#         j += 1
#     i += 1
#     print()
#
# print('----------------------------------------------------')
#
# i = 0
# while i < 10:
#     i += 1
#     j = 10
#     while i < j:
#         print('*', end=' ')
#         j -= 1
#
#     print()

# 九九乘法表
# i = 0
# # while i < 9:
# #     i += 1
# #     j = 0
# #     while j < i:
# #         j += 1
# #         print('{0} * {1} = {2}'.format(j, i, i * j), end=' ')
# #     print()
from time import *
start = time()
i = 2
while i <= 100:
    j = 2
    flag = False
    while j <= i**0.5:
        if i % j == 0:
            flag = True
            break
        j += 1
    if flag:
        pass
    #     print(f'{i}是合数')
    # else:
    #     print(f'{i}是质数')
    i += 1
end = time()
f = end - start
print(f)



