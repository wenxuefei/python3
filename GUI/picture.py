"""
    画图软件
"""
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.colorchooser import *
import webbrowser
import random

# 主窗口的宽度和高度
win_width = 900
win_height = 450


class Application(Frame):
    """
        画图软件
    """

    def __init__(self, master=None, bgcolor="#000000"):
        super().__init__(master)  # super() 父类的定义，非父类对象 初始化父类构造器
        self.master = master
        self.bgcolor = bgcolor
        self.x = 0
        self.y = 0
        self.fgcolor = "red"
        self.lastDraw = 0
        self.startDrawFlag = False
        self.pack()  # 布局管理器进行布局和显示
        self.create_widget()

    def create_widget(self):
        """
            创建绘图区域
        """

        self.drawPad = Canvas(self, width=win_width, height=win_height * 0.9, bg=self.bgcolor)
        self.drawPad.pack()

        # 创建按钮
        btn_start = Button(self, text="开始", name="start")
        btn_start.pack(side="left", padx=10)

        btn_pen = Button(self, text="画笔", name="pen")
        btn_pen.pack(side="left", padx=10)

        btn_rect = Button(self, text="矩形", name="rect")
        btn_rect.pack(side="left", padx=10)

        btn_clear = Button(self, text="清屏", name="clear")
        btn_clear.pack(side="left", padx=10)

        btn_erasor = Button(self, text="橡皮檫", name="erasor")
        btn_erasor.pack(side="left", padx=10)

        btn_line = Button(self, text="直线", name="line")
        btn_line.pack(side="left", padx=10)

        btn_lineArrow = Button(self, text="箭头直线", name="lineArrow")
        btn_lineArrow.pack(side="left", padx=10)

        btn_color = Button(self, text="颜色", name="color")
        btn_color.pack(side="left", padx=10)

        # 事件处理
        btn_pen.bind_class("Button", "<Button-1>", self.eventManger)
        self.drawPad.bind("<ButtonRelease-1>", self.stopDraw)

        # 增加颜色切换快捷键
        root.bind("<KeyPress-r>", self.kuai)
        root.bind("<KeyPress-g>", self.kuai)
        root.bind("<KeyPress-y>", self.kuai)

    def eventManger(self, event):
        name = event.widget.winfo_name()
        print(name)
        if name == "line":
            self.drawPad.bind("<B1-Motion>", self.myline)
        elif name == "lineArrow":
            self.drawPad.bind("<B1-Motion>", self.myLineArrow)
        elif name == "rect":
            self.drawPad.bind("<B1-Motion>", self.myRect)
        elif name == "pen":
            self.drawPad.bind("<B1-Motion>", self.myPen)
        elif name == "erasor":
            self.drawPad.bind("<B1-Motion>", self.myErasor)
        elif name == "clear":
            self.drawPad.delete("all")
        elif name == "color":
            c = askcolor(title="选择颜色", color=self.fgcolor)
            self.fgcolor = c[1]

    def myline(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawPad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)

    def myLineArrow(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawPad.create_line(self.x, self.y, event.x, event.y, arrow=LAST, fill=self.fgcolor)

    def myRect(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawPad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fgcolor)

    def myPen(self, event):
        self.startDraw(event)
        self.drawPad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)
        self.x = event.x
        self.y = event.y

    def myErasor(self, event):
        self.startDraw(event)
        self.drawPad.create_rectangle(event.x - 10, event.y - 10, event.x, event.y, fill=self.bgcolor)

        self.x = event.x
        self.y = event.y

    def stopDraw(self, event):
        self.startDrawFlag = False
        self.lastDraw = 0

    def startDraw(self, event):
        self.drawPad.delete(self.lastDraw)  # 删除上次左后坐标点

        if not self.startDrawFlag:
            self.startDrawFlag = True
            self.x = event.x
            self.y = event.y

    def kuai(self, event):
        if event.char == "r":
            self.fgcolor = "#ff0000"
        elif event.char == "g":
            self.fgcolor = "#00ff00"
        elif event.char == "y":
            self.fgcolor = "#ffff00"


if __name__ == '__main__':  # 将此程序作为独立程序
    root = Tk()
    root.title("记事本")
    root.geometry(str(win_width) + "x" + str(win_height) + "+200+300")
    app = Application(master=root)  # 主窗口对象

    root.mainloop()
