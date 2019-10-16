"""
    记事本小程序
"""
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.colorchooser import *
import webbrowser
import random


class Application(Frame):
    """
        记事本
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
        menuFile.add_command(label="新建", accelerator="ctrl+n", command=self.newFile)
        menuFile.add_command(label="打开", accelerator="ctrl+o", command=self.openFile)
        menuFile.add_command(label="保存", accelerator="ctrl+s", command=self.saveFile)
        menuFile.add_separator()  # 添加分割线
        menuFile.add_command(label="退出", accelerator="ctrl+q", command=self.exit)

        # 将主菜单添加到根窗口
        root['menu'] = menubar

        # 增加快捷键
        root.bind("<Control-n>", lambda event: self.newFile())
        root.bind("<Control-o>", lambda event: self.openFile())
        root.bind("<Control-s>", lambda event: self.saveFile())
        root.bind("<Control-q>", lambda event: self.exit())

        # 文本编辑区
        self.textpad = Text(root, width=50, height=30)
        self.textpad.pack(side="left")

        # 创建上下文菜单
        self.contextMenu = Menu(root)
        self.contextMenu.add_command(label="背景颜色", command=self.openAskColor)

        # 为右键绑定事件
        root.bind("<Button-3>", self.createContentMenu)

    def newFile(self):
        self.filename = asksaveasfilename(title="另存为", initialfile="未命名.txt", filetypes=[("文本文档", "*.txt")],
                                          defaultextension=".txt")
        self.saveFile()

    def openFile(self):
        self.textpad.delete(1.0, END)  # 把text控件中所有的内容清空
        with askopenfile(title="打开文本文件") as f:
            # print(f.read())
            self.textpad.insert(INSERT, f.read())
            self.filename = f.name

    def saveFile(self):
        with open(self.filename, 'w') as f:
            c = self.textpad.get(1.0, END)
            f.write(c)

    def exit(self):
        root.quit()

    def openAskColor(self):
        s1 = askcolor(title="选择背景色", color="red")
        self.textpad.config(bg=s1[1])

    def createContentMenu(self, event):
        # 菜单在鼠标右击的坐标出显示
        self.contextMenu.post(event.x_root, event.y_root)


if __name__ == '__main__':  # 将此程序作为独立程序
    root = Tk()
    root.title("记事本")
    root.geometry("450x300+200+300")
    app = Application(master=root)  # 主窗口对象

    root.mainloop()
