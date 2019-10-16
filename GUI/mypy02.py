"""
    测试一个经典的GUI程序的写法，使用面向对象的方式
"""
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.colorchooser import *
import webbrowser
import random


# Options 选项
# 1. 创建对象时，使用命名参数 eg: fred=Button(self,text="wen",dict(text="Love", width=10, height=2, bg="black", fg="white"))
# 2. 创建对象后，使用字典索引 self.btn01 = Button(self)  # 创建按钮
#         self.btn01["text"] = '点击送花'
#         self.btn01.pack()
#         self.btn01["command"] = self.songhua
# 3. 创建对象后使用config() 方法 fred.config(text="Love", width=10, height=2, bg="black", fg="white")

class Application(Frame):
    """
        一个经典的GUI程序的类的写法
    """

    def __init__(self, master=None):
        super().__init__(master)  # super() 父类的定义，非父类对象 初始化父类构造器
        self.master = master
        self.textpad = None  # textpad 表示Text 文本对象
        self.pack()  # 布局管理器进行布局和显示
        self.create_widget()

    def create_widget(self):
        """
            创建组件
        """
        # self.btn01 = Button(self)  # 创建按钮
        # self.btn01["text"] = '点击送花'
        # self.btn01.pack()
        # self.btn01["command"] = self.songhua
        #
        # # 创建退出按钮
        # self.btnQuit = Button(self, text="退出", command=root.destroy)
        # self.btnQuit.pack()
        #
        # global photo1
        # photo1 = PhotoImage(file='image/start.gif')
        # self.btn02 = Button(self, image=photo1, command=self.login)
        # self.btn02.pack()
        # self.btn02.config(state="disable")
        #
        # self.btn03 = Button(self, text="登录", width=6, height=3, anchor=E, command=self.login)
        # self.btn03.pack()
        #
        # self.label01 = Label(self, dict(text="Love", width=10, height=2, bg="black", fg="white"))
        # self.label01.pack()
        #
        # self.label02 = Label(self, text="wen", width=10, height=2, bg="blue", fg="white", font=("黑体", 30))
        # self.label02.pack()
        #
        # # 显示图像
        # global photo  # 将photo 定义为全局变量，局部变量，方法执行完，图像对象销毁，窗口不显示
        # photo = PhotoImage(file="image/a.gif")
        # self.label03 = Label(self, image=photo)
        # self.label03.pack()
        #
        # # 创建多行文本
        # self.label04 = Label(self, text="文行行行\n倪妮的大幅度\n绝地刀锋\n", borderwidth=5, relief="groove", justify="right")
        # self.label04.pack()

        # 创建登录界面的组件
        # self.label01 = Label(self, text="用户名")
        # self.label01.pack()

        # Entry 单行文本框
        # StringVal 变量绑定到指定的组件
        # StringVal 变量的值发生变化，组件内容也发生变化
        # 组件内容发生变化，变量的值也发生变化
        # v1 = StringVar()
        # self.entry01 = Entry(self, textvariable=v1)
        # self.entry01.pack()
        # v1.set("admin")
        #
        # self.label02 = Label(self, text="密码")
        # self.label02.pack()
        #
        # v2 = StringVar()
        # self.entry02 = Entry(self, textvariable=v2, show="*")
        # self.entry02.pack()
        #
        #
        #
        # self.btn01 = Button(self, text="登录", command=self.login)
        # self.btn01.pack()

        # 多行文本框
        # self.w1 = Text(self, width=40, height=12, bg="gray")
        # self.w1.pack()
        #
        # self.w1.insert(1.0, "0123456789\nabcdefg")
        # self.w1.insert(2.3, "锄禾日当午，汗滴禾下土。谁知盘中餐，粒粒皆辛苦。\n")
        #
        # Button(self, text="重复输入文本", command=self.insertText).pack(side="left")
        # Button(self, text="返回文本", command=self.returnText).pack(side="left")
        # Button(self, text="添加图片", command=self.addImage).pack(side="left")
        # Button(self, text="添加组件", command=self.addWidget).pack(side="left")
        # Button(self, text="通过tag精确控制文本", command=self.testTag).pack(side="left")
        #
        # # 单选按钮 和 复选按钮
        # self.v = StringVar()
        # self.v.set("F")
        #
        # self.r1 = Radiobutton(self, text="男性", value="M", variable=self.v)
        # self.r2 = Radiobutton(self, text="女性", value="F", variable=self.v)
        #
        # self.r1.pack(side="left")
        # self.r2.pack(side="left")
        #
        # self.codeHobby = IntVar()
        # self.videoHobby = IntVar()
        #
        # self.c1 = Checkbutton(self, text="敲代码", onvalue=1, variable=self.codeHobby)
        # self.c1.pack(side="left")
        # self.c2 = Checkbutton(self, text="看电影", onvalue=1, variable=self.videoHobby)
        # self.c2.pack(side="left")
        #
        # Button(self, text="确定", command=self.confirm).pack(side="left")

        # canvas
        # self.canvas = Canvas(self, width=300, height=200, background="green")
        # self.canvas.pack()
        #
        # # 画一条直线 10,10 为一个坐标
        # line = self.canvas.create_line(10, 10, 30, 20, 40, 50)
        # # 画一个矩形
        # rect = self.canvas.create_rectangle(50, 50, 100, 100)
        # # 画一个椭圆，坐标两双。为椭圆的边界矩形左上角和底部右下角
        # oval = self.canvas.create_oval(50, 50, 100, 100)
        #
        # global photo
        # photo = PhotoImage(file="image/start.gif")
        # self.canvas.create_image(150, 170, image=photo)
        # Button(self, text="画10个矩形", command=self.darw50Recq).pack()

        # 布局管理器
        # 通过grid实现登录界面
        # self.label01 = Label(self, text="用户名")
        # self.label01.grid(row=0, column=0)
        #
        # self.entry01 = Entry(self)
        # self.entry01.grid(row=0, column=1)
        # Label(self, text="用户名为手机号").grid(row=0, column=2)
        #
        # self.label02 = Label(self, text="密码")
        # self.label02.grid(row=1, column=0)
        #
        # self.entry02 = Entry(self, show="*")
        # self.entry02.grid(row=1, column=1)
        #
        # self.btn01 = Button(self, text="登录", command=self.login)
        # self.btn01.grid(row=2, column=1, sticky=EW)
        # self.btn02 = Button(self, text="取消", command=self.login)
        # self.btn02.grid(row=2, column=2, sticky=E)

        # grid 布局实现计算器界面
        # btnText = (("MC", "M+", "M-", "MR"),
        #            ("C", "±", "÷", "×"),
        #            (7, 8, 9, "-"),
        #            (4, 5, 6, "+"),
        #            (1, 2, 3, "="),
        #            (0, "."))
        #
        # Entry(self).grid(row=0, column=0, columnspan=4, pady=10)
        #
        # for rindex, r in enumerate(btnText):
        #     for cindex, c in enumerate(r):
        #         if c == "=":
        #             Button(self, text=c, width=2, borderwidth=1,
        #                    relief="raised").grid(row=rindex + 1, column=cindex, sticky=NSEW,
        #                                          rowspan=2, padx=2, pady=2)
        #         elif c == 0:
        #             Button(self, text=c, width=2, borderwidth=1,
        #                    relief="raised").grid(row=rindex + 1, column=cindex, sticky=NSEW, columnspan=2, padx=2,
        #                                          pady=2)
        #         elif c == ".":
        #             Button(self, text=c, width=2, borderwidth=1,
        #                    relief="raised").grid(row=rindex + 1, column=cindex + 1, sticky=NSEW, padx=2, pady=2)
        #         else:
        #             Button(self, text=c, width=2, borderwidth=1,
        #                    relief="raised").grid(row=rindex + 1, column=cindex, sticky=NSEW, pady=2, padx=2)

        # 菜单栏
        # 创建主菜单
        menubar = Menu(root)

        # 创建子菜单
        menuFile = Menu(menubar)
        menuEdit = Menu(menubar)
        menuHelp = Menu(menubar)

        # 将子菜单加入到主菜单栏
        menubar.add_cascade(label="文件(F)", menu=menuFile)
        menubar.add_cascade(label="编辑(E)", menu=menuEdit)
        menubar.add_cascade(label="文件(H)", menu=menuHelp)

        # 添加菜单项
        menuFile.add_command(label="新建", accelerator="ctrl+n", command=self.test)
        menuFile.add_command(label="打开", accelerator="ctrl+o", command=self.test)
        menuFile.add_command(label="保存", accelerator="ctrl+s", command=self.test)
        menuFile.add_separator()  # 添加分割线
        menuFile.add_command(label="推出", accelerator="ctrl+q", command=self.test)

        # 将主菜单添加到根窗口
        root['menu'] = menubar

        # 文本编辑区

        # 创建上下文菜单
        self.contextMenu = Menu(root)
        self.contextMenu.add_command(label="背景颜色", command=self.test)

        # 为右键绑定事件
        root.bind("<Button-3>", self.createContentMenu)

    def test(self):
        print(111)

    def createContentMenu(self, event):
        # 菜单在鼠标右击的坐标出显示
        self.contextMenu.post(event.x_root, event.y_root)

    def darw50Recq(self):
        for i in range(0, 10):
            # 生成随机数为0 到 canvas宽度一半的随机数
            x1 = random.randrange(int(self.canvas['width']) / 2)
            y1 = random.randrange(int(self.canvas['height']) / 2)
            x2 = x1 + random.randrange(int(self.canvas['height']) / 2)
            y2 = y1 + random.randrange(int(self.canvas['height']) / 2)
            self.canvas.create_rectangle(x1, y1, x2, y2)

    def confirm(self):
        if self.videoHobby.get() == 1:
            messagebox.showinfo("提示", "你喜欢看电影")
        if self.codeHobby.get() == 1:
            messagebox.showinfo("提示", "你喜欢敲代码")
        messagebox.showinfo("测试", "选择的性别：" + self.v.get())

    def insertText(self):
        # INSERT 索引表示在光标处插入
        self.w1.insert(INSERT, '问 ')
        # END 索引表示在最后插入
        self.w1.insert(END, '你好 ')

    def returnText(self):
        # Indexes(索引)是用来指向Text组件中文本的位置，Text的最贱索引也是对应实际字符之间的位置
        # 核心：行号以1开始 列号以0 开始
        print(self.w1.get(1.2, 1.6))
        self.w1.insert(1.8, '问 ')
        print("所有文本内容：\n" + self.w1.get(1.0, END))

    def addImage(self):
        # global photo
        self.photo = PhotoImage(file="image/a.gif")
        self.w1.image_create(END, image=self.photo)

    def addWidget(self):
        b1 = Button(self.w1, text="love")
        # 在text创建组件的命令
        self.w1.window_create(INSERT, window=b1)

    def testTag(self):
        self.w1.delete(1.0, END)
        self.w1.insert(INSERT, "gkoper\nkopwek\nropwerpoe\n百度 ekopre")
        self.w1.tag_add("good", 1.0, 1.9)
        self.w1.tag_config("good", background="yellow", foreground="red")

        self.w1.tag_add("baidu", 4.0, 4.2)
        self.w1.tag_config("baidu", underline=True)
        self.w1.tag_bind("baidu", "<Button-1>", self.webshow)

    def webshow(self, event):
        webbrowser.open('https://www.baidu.com')

    def songhua(self):
        messagebox.showinfo("送花", "送你99朵玫瑰花")

    def login(self):
        username = self.entry01.get()
        password = self.entry02.get()

        print("用户名：", username)
        print("密码  ：", password)

        if username == 'admin' and password == '123456':
            messagebox.showinfo("系统提示", "您已登录成功！！！")
        else:
            messagebox.showinfo("系统提示", "登录失败，用户名或密码错误！！！")


if __name__ == '__main__':  # 将此程序作为独立程序
    root = Tk()
    root.title("一个经典的GUI程序的测试")
    root.geometry("200x240+200+300")
    app = Application(master=root)  # 主窗口对象

    root.mainloop()
