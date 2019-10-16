import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# # 绘制直线
# # 准备绘制的两个点（1，2）（4，8）
#
# # 调用绘制方法
# plt.plot((1, 4), (2, 8))
# # 显示绘制图
# plt.show()

# # 绘制折线
# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]
# plt.plot(x,y)
# plt.show()

# 设置样式
# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]
# plt.plot(x, y, linewidth=5)  # 线条宽度
# # 添加x,y轴名称
# plt.xlabel('x')
# plt.ylabel('y=x^2')
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标题
# plt.title('多个点绘制折线图')
# plt.show()

# 绘制曲线
# x = range(-100,100)
# y = [i**2 for i in x]
# plt.plot(x,y)
# # 保存为图片
# plt.savefig('result')
# # plt.savefig('result.jpg')
# plt.show()

# 绘制正弦，余弦,正切
# 生成0-10之间100个等差数
# x = np.linspace(0, 10, 100)
# sin_y = np.sin(x)
# cos_y = np.cos(x)
# tan_y = np.tan(x)
# plt.plot(x,sin_y)
# plt.plot(x,cos_y)
# plt.plot(x,tan_y)
# plt.show()

# # 分区域
# x = np.linspace(0, 10, 100)
# sin_y = np.sin(x)
#
# # 将画布分为两行两列，画到区1
# plt.subplot(2, 2, 1)
# # 修改x,y轴的坐标
# plt.xlim(-5, 20)
# plt.ylim(-2, 2)
# plt.plot(x, sin_y)
#
# cos_y = np.cos(x)
# plt.subplot(2, 2, 4)
# plt.plot(x, cos_y)
# plt.show()

# 绘制散点图
# x = np.linspace(0, 10, 100)
# sin_y = np.sin(x)
# plt.scatter(x,sin_y)
# plt.plot(x,sin_y,'o') # plot 绘制速度优于scatter
# plt.show()

# # 绘制10种大小100种颜色不同的点
# np.random.seed(0)  # 执行多次每次获取的随机数为一样的
# x = np.random.rand(100)
# y = np.random.rand(100)
# # 生成10种大小
# size = np.random.rand(10) * 1000
# color = np.random.rand(100)
# # 点的个数和颜色个数应相同
# plt.scatter(x, y, s=size, c=color,alpha=0.7)  # s表示点的大小 c表示颜色 alpha 表示透明度
# plt.show()

# # 绘制不同颜色的线 添加图例legend 默认位置在左上角 loc修改位置
# x = np.linspace(0, 10, 100)
# plt.plot(x, x + 0, '--g', label='--g')
# plt.plot(x, x + 1, '-.r', label='-.r')
# plt.plot(x, x + 2, ':b', label=':b')
# plt.plot(x, x + 3, '.k', label='.k')
# plt.plot(x, x + 4, ',c', label=',c')
# plt.plot(x, x + 5, '*', label='*')
# plt.legend(loc='upper right', fancybox=True, framealpha=0.5, shadow=True, borderpad=1)
# plt.show()

# # 绘制柱状图 （x:年份，y:对应的销量）
# x = [1980, 1985, 1990, 1995]
# y = [1000, 2000, 3000, 4000]
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标题
# x_labels = ['1980年', '1985年', '1990年', '1995年']
#
# plt.xlabel('年份')
# plt.ylabel('销量')
# # 修改x坐标的值
# plt.xticks(x, x_labels)
#
# plt.title('根据年份销量对比图')
#
# plt.bar(x, y, width=3)
# plt.show()

# np.random.seed(0)
# x = np.arange(5)
# y = np.random.randint(-5, 5, 5)
# plt.subplot(1, 2, 1)
# # 显示不同颜色 小于0显示绿色
# v_bar = plt.bar(x, y, color='blue')
# for bar,height in zip(v_bar,y):
#     if height < 0:
#         bar.set(color='green')
# # 在0位置添加线条
#
# plt.axhline(0, color='blue', linewidth=2)
# plt.subplot(1, 2, 2)
# plt.axvline(0, color='red', linewidth=2)
# plt.barh(x, y, color='red')
# plt.show()

# real_name = ['千与千寻', '玩具总动员4', '黑衣人:全球通缉']
# real_num1 = [7548, 4013, 1673]
# real_num2 = [5453, 1840, 1080]
# real_num3 = [4348, 2345, 1348]
# x = np.arange(len(real_name))
# width = 0.2
# plt.bar([i for i in x], real_num1, alpha=0.5, width=width,label=real_name[0])
# plt.bar([i + width for i in x], real_num2, alpha=0.5, width=width,label=real_name[1])
# plt.bar([i + width * 2 for i in x], real_num3, alpha=0.5, width=width,label=real_name[2])
#
# # 设置x坐标的值
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标题
# x_labels = ['第{}天'.format(i + 1) for i in x]
# plt.xticks([i + width for i in x], x_labels)
# # 添加ylabel
# plt.ylabel('票房')
# #添加图例
# plt.legend()
# plt.title('三日票房排行对比')
# plt.show()

# 绘制饼状图
# man = 71351
# woman = 68187
#
# man_per = man / (man + woman)
# woman_per = woman / (man + woman)
#
# # 添加颜色
# colors = ['blue', 'red']
#
# # 添加名称
# labels = ['男', '女']
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标题
# paches, texts, autotexts = plt.pie([man_per, woman_per], labels=labels, colors=colors, explode=(0, 0.05),
#                                    autopct='%0.1f%%')
#
# # 设置饼状图中的字体颜色
# for text in autotexts:
#     text.set_color('white')
#
# # 设置字体大小
# for text in texts + autotexts:
#     text.set_fontsize(20)
#
# plt.show()

# # 绘制直方图
# # 正太分布
# # x = np.random.randn(1000)
# x = np.random.normal(0, 0.8, 1000)  # 指定期望和均值的正太分布
# y = np.random.normal(-2, 1, 1000)  # 指定期望和均值的正太分布
# z = np.random.normal(2, 3, 1000)  # 指定期望和均值的正太分布
# kwargs = dict(bins=100, alpha=0.5)
# plt.hist(x, **kwargs)  # 10个柱子装在一起
# plt.hist(y, **kwargs)  # 10个柱子装在一起
# plt.hist(z, **kwargs)  # 10个柱子装在一起
# plt.show()

# # 绘制等高线图
# x = np.linspace(-10, 10, 100)
# y = np.linspace(-10, 10, 100)
#
# # 计算x,y 相交的点a
# X, Y = np.meshgrid(x, y)
#
# # 计算Z的坐标
# Z = np.sqrt(X ** 2 + Y ** 2)
# plt.contourf(X, Y, Z)
# plt.contour(X, Y, Z)
# plt.show()

# 绘制三维图
# X = [1, 1, 2, 2]
# Y = [3, 4, 4, 3]
# Z = [1, 100, 1, 1]
#
# # 创建Axes3D对象
# figure = plt.figure()
# ax = Axes3D(figure)
# ax.plot_trisurf(X, Y, Z)

fig = plt.figure()
# 创建3d图形的两种方式
# ax = Axes3D(fig)
ax = fig.add_subplot(111, projection='3d')
# X, Y value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)    # x-y 平面的网格
R = np.sqrt(X ** 2 + Y ** 2)
# height value
Z = np.sin(R)
# rstride:行之间的跨度  cstride:列之间的跨度
# rcount:设置间隔个数，默认50个，ccount:列的间隔个数  不能与上面两个参数同时出现
#vmax和vmin  颜色的最大值和最小值
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
# zdir : 'z' | 'x' | 'y' 表示把等高线图投射到哪个面
# offset : 表示等高线图投射到指定页面的某个刻度
ax.contourf(X,Y,Z,zdir='z',offset=-2)
# 设置图像z轴的显示范围，x、y轴设置方式相同
ax.set_zlim(-2,2)

plt.show()
