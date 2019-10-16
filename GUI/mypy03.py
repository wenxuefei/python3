# coding = utf-8
# # 测试pack布局管理
#
from tkinter import *
from tkinter.colorchooser import *  # 颜色选择器
from tkinter.filedialog import *  # 文件上传
from tkinter.simpledialog import *
from tkinter.messagebox import *

#
# # Frame 是一个矩形区域，就是用来放置其他组件
# f1 = Frame(root)
# f1.pack()
#
# f2 = Frame(root)
# f2.pack()
#
# btnText = ("流行风", "中国风", "日本风", "重金属", "轻音乐")
#
# for text in btnText:
#     Button(f1,text=text).pack(side="left",padx=10)
#
# for i in range(1,20):
#     Label(f2,width=5,height=10,borderwidth=1,relief="solid",bg="black" if i%2==0 else "white").pack(side="left",padx=2)
#
# root.mainloop()

# place 管理布局

# root.geometry("500x300")
# root.title("布局管理place")
# root["bg"] = "white"
#
# f1 = Frame(root, width=200, height=200, bg="green")
# f1.place(x=30, y=30)
#
# Button(root, text="问1").place(relx=0.2, x=100, y=20, relwidth=0.2, relheight=0.5)
# Button(f1, text="问2").place(relx=0.6, rely=0.7)
# Button(f1, text="问3").place(relx=0.5, rely=0.2)
# root.mainloop()

# place 扑克小游戏示例

# class Application(Frame):
#
#     def __init__(self, master=None):
#         super().__init__(master)  # super() 父类的定义，非父类对象 初始化父类构造器
#         self.master = master
#         self.pack()  # 布局管理器进行布局和显示
#         self.create_widget()
#
#     def create_widget(self):
#         """
#             创建组件
#         """
#         # self.photo = PhotoImage(file="image/puke/puke1.gif")
#         self.photos = [PhotoImage(file="image/puke/puke" + str(i + 1) + ".gif") for i in range(10)]
#
#         self.pukes = [Label(self.master, image=self.photos[i]) for i in range(10)]
#         for i in range(10):
#             self.pukes[i].place(x=10 + i * 40, y=50)
#
#         # 为所有的label添加时间处理
#         self.pukes[0].bind_class("Label", "<Button-1>", self.chupai)
#
#     def chupai(self, event):
#         print(event.widget.winfo_geometry())
#         print(event.widget.winfo_y())
#         if event.widget.winfo_y() == 50:
#             event.widget.place(y=30)
#         else:
#             event.widget.place(y=50)
#
#
# if __name__ == '__main__':  # 将此程序作为独立程序
#     root = Tk()
#     root.title("一个经典的GUI程序的测试")
#     root.geometry("600x270+200+300")
#     app = Application(master=root)  # 主窗口对象
#
#     root.mainloop()  # 包含消息循环

root = Tk()
root.geometry("600x270+200+300")

c1 = Canvas(root, width=200, height=200, bg="green")
c1.pack()


# def mouseTest(event):
#     print("鼠标左键单击位置，相当于父容器：{0}，{1}".format(event.x, event.y))
#     print("鼠标左键单击位置，相当于屏幕：{0}，{1}".format(event.x_root, event.y_root))
#     print("事件绑定的组件：{0}".format(event.widget))
#
#
# def testDrag(event):
#     c1.create_oval(event.x, event.y, event.x + 1, event.y + 1)
#
#
# def keybordTest(event):
#     print("键的keybordcode:{0},键的char：{1},键的keysym：{2}".format(event.keycode, event.char, event.keysym))
#
#
# def press_a_test(event):
#     print("press a")
#
#
# def release_a_test(event):
#     print("release a")
#
#
# def monuseTest1():
#     print("command 方法，简单情况下不涉及获取event对象，可以使用")
#
#
# def monuseTest2(a, b):
#     print("a={0},b={1}".format(a, b))
#
#
# def monuseTest(event):
#     print("右键点击事件，绑定所有按钮")
#     print(event.widget)


# def test1():
#     print("最喜欢的人：", v.get())


# def test2(value):
#     print("滑块的值：", value)
#     newFont = ("宋体", value)
#     # a.config(font=newFont)


# def test3():
#     s2 = askcolor(color="red", title="选择背景色")
#     print(s2)
#     # s2 的值是： ((0.0,0.0,255.99609375),#0000ff)
#     root.config(bg=s2[1])
#
#
# def test4():
#     # f = askopenfile(title="上传文件", initialdir="e:", filetypes=[("视频文件", ".MP4")])
#     # show["text"] = f
#     with askopenfile(title="上传文件", initialdir="e:", filetypes=[("视频文件", ".txt")]) as f:
#         show["text"] = f.read()

def test5():
    a = askinteger(title="输入年龄", prompt="请输入年龄", initialvalue=18, minvalue=1, maxvalue=150)
    show['text'] = a


# c1.bind("<Button-1>", mouseTest)
# c1.bind("<B1-Motion>", testDrag)
#
# root.bind("<KeyPress>", keybordTest)
# root.bind("<KeyPress-a>", press_a_test)
# root.bind("<KeyRelease-a>", release_a_test)
#
# b1 = Button(root, text="测试Command1", command=monuseTest1)
# b1.pack(side="left")
# b2 = Button(root, text="测试Command2", command=lambda: monuseTest2("aa", "bb"))
# b2.pack(side="left")
#
# # 给所有按钮绑定右键单击事件<Button-3> 或 3
# b1.bind_class("Button", "<Button-3>", monuseTest)


# optionMenu组件 和 Scale 移动滑块

# v = StringVar(root)
# v.set("wen")
# om = OptionMenu(root, v, "wen1", "wen", "wen2")
# om['width'] = 10
# om.pack()
#
# Button(root, text="确定", command=test1).pack()
#
# # orient 显示方式 默认垂直 HORIZONTAL（水平）tickinterval 间隔值
# s1 = Scale(root,from_=10, to=50, length=200, tickinterval=5, orient=HORIZONTAL, command=test2)
# s1.pack()
#
# a = Label(root, text="I Love You", width=10, height=1, bg="black", fg="white")
# a.pack()

# 颜色选择器
# Button(root, text="颜色选择器", command=test3).pack()

# 文本选择器
# Button(root, text="选择编辑传输的文件", command=test4).pack()
# show = Label(root, width=100, height=3, bg="green")
# show.pack()

# 简单对话框
# Button(root, text="请输入你的年龄", command=test5).pack()

# 通用消息框
# al = showinfo(title="i love you ",message="学好数理化\n走遍天下都不怕")
# print(al)
# root.mainloop()

# 组件对象的绑定 1.通过command属性绑定（适合简单不获取event对像） 2.bind() 方法绑定，（适合获取event对象）
# 组件类绑定 bind_class() 方法 将该组件类所有的组件绑定事件
