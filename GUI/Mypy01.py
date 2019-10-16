from tkinter import *
from tkinter import messagebox

# 创建主窗口对象
root = Tk()

root.title("我的第一个GUI程序")  # 程序名称

# 第一个为宽度(500) 第二个位高度(300) 第三个距离屏幕左边(100) 第四个距离屏幕上边(200) x 为小写字母x
root.geometry("500x300+100+200")


btn01 = Button(root)  # 创建按钮对象，将窗口对象传入
btn01["text"] = "点我就送花"
btn01.pack()  # 压缩窗口


def songhua(e):  # e 点击事件对象
    messagebox.showinfo("Message", "送你一朵花，感谢我吧")  # 第一个参数标题 第二个内容
    print(e)


btn01.bind("<Button-1>", songhua)  # 按钮事件绑定  button-1 左键点击

root.mainloop()  # 调用组件的mainloop()方法 进行事件循环
