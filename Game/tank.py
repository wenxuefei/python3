"""
坦克大战游戏的需求
1.项目中有哪些类
2.每个类中有哪些方法

1.坦克类（我方坦克、敌方坦克）
  射击
  移动类
  显示坦克的方法
2.子弹类
   移动
   显示子弹的方法
3.墙壁类
   属性：是否可以通过
4.爆炸效果类
  展示爆炸效果
5.音效类
  播放音乐
6.主类
  开始游戏
  结束游戏
"""
# encoding = utf-8
# 导入pygame模块
import pygame
import time
import random

from pygame.sprite import Sprite

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)


# 定义一个基类,碰撞检测
class BaseItem(Sprite):
    def __int__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)


# 主类
class MainGame:
    window = None
    my_tank = None

    enemyTankList = []  # 坦克列表
    enemyTankCount = 5  # 坦克数量

    myBulletList = []  # 我方子弹的列表

    enmeyBulletList = []  # 敌方子弹列表

    exploadList = []  # 子弹爆炸效果列表

    wallList = []  # 存储墙壁的列表

    def __init__(self):
        pass

    # 开始游戏
    def startGame(self):
        # 加载主窗口
        pygame.display.init()

        # 设置窗口的大小及显示
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # 设置窗口的标题
        pygame.display.set_caption("坦克大战")

        # 初始化我方坦克

        self.createMyTank()

        # 初始化敌方坦克，并放入到敌方列表
        self.createEnemyTank()

        # 初始化墙壁
        self.createWall()

        while True:

            # 使用坦克移动的速度慢一点
            time.sleep(0.02)

            # 给窗口设置填充色
            MainGame.window.fill(BG_COLOR)

            # 获取事件
            self.getEvent()

            # 绘制文字
            MainGame.window.blit(self.getTextSurface("剩余敌方坦克%d辆" % len(MainGame.enemyTankList)), (5, 5))

            # 调用坦克显示方法
            if MainGame.my_tank and MainGame.my_tank.live:
                MainGame.my_tank.displayTank()
            else:
                # 删除坦克
                del MainGame.my_tank
                MainGame.my_tank = None
            # 循环遍历敌方坦克列表，展示敌方坦克
            self.blitEnemy()

            # 循环遍历我方子弹列表，展示敌方子弹
            self.blitEnemyBullet()

            # 循环遍历爆炸列表，展示爆炸效果
            self.blitExplode()

            # 循环遍历墙壁列表
            self.blitWall()

            # 循环遍历显示我方子弹
            self.blitMyBullet()

            # 调用移动方法
            # 如果坦克的开关是开启，才可以移动
            if MainGame.my_tank and MainGame.my_tank.live:
                if not MainGame.my_tank.stop:
                    MainGame.my_tank.move()
                    # 检测坦克是否与墙壁发生碰撞
                    MainGame.my_tank.hitWall()
                    # 检测我方坦克与敌方坦克发生碰撞
                    MainGame.my_tank.myTank_hit_enemyTank()

            pygame.display.update()

    # 结束游戏
    def endGame(self):
        print("谢谢使用")
        # 结束python解释器
        exit()

    # 获取事件
    def getEvent(self):
        # 获取所有事件
        eventList = pygame.event.get()

        # 遍历事件
        for event in eventList:
            # 判断event.type 是否QUIT，如果是退出的话，直接调用程序结束方法
            if event.type == pygame.QUIT:
                self.endGame()

            # 如果是键盘的按下
            if event.type == pygame.KEYDOWN:
                # 当坦克不存在活着死亡
                if not MainGame.my_tank:
                    # 判断按下的是否为ESC
                    if event.key == pygame.K_ESCAPE:
                        # 让坦克重生
                        self.createMyTank()

                if MainGame.my_tank and MainGame.my_tank.live:
                    # 判断是上下左右 具体是哪一个按键的处理
                    if event.key == pygame.K_LEFT:
                        # 切换方向
                        MainGame.my_tank.direction = "L"

                        # 修改坦克的开关状态
                        MainGame.my_tank.stop = False

                        MainGame.my_tank.move()
                        print("按下左键")

                    elif event.key == pygame.K_RIGHT:
                        MainGame.my_tank.direction = "R"

                        # 修改坦克的开关状态
                        MainGame.my_tank.stop = False

                        MainGame.my_tank.move()
                        print("按下右键")
                    elif event.key == pygame.K_UP:
                        MainGame.my_tank.direction = "U"

                        # 修改坦克的开关状态
                        MainGame.my_tank.stop = False

                        MainGame.my_tank.move()
                        print("按下上键")
                    elif event.key == pygame.K_DOWN:
                        MainGame.my_tank.direction = "D"

                        # 修改坦克的开关状态
                        MainGame.my_tank.stop = False

                        MainGame.my_tank.move()
                        print("按下下键")
                    elif event.key == pygame.K_SPACE:
                        # 如果当前我方子弹列表的大小 小于3 才可以创建
                        # 创建子弹
                        if len(MainGame.myBulletList) < 3:
                            myBullet = Bullet(MainGame.my_tank)
                            MainGame.myBulletList.append(myBullet)

                            music = Music('img/fire.wav')
                            music.play()

                            print("发射子弹")

            # 松开方向键停止
            if event.type == pygame.KEYUP:
                # 判断松开的键具体是方向键才停止移动
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    if MainGame.my_tank and MainGame.my_tank.live:
                        MainGame.my_tank.stop = True

    # 左上角文字的绘制
    def getTextSurface(self, text):
        # 初始化字体
        pygame.font.init()

        # 查看所有的字体名称
        # print(pygame.font.get_fonts())

        # 获取字体font对象
        font = pygame.font.SysFont("kaiti", 18)

        # 绘制文字信息
        textSurface = font.render(text, True, TEXT_COLOR)

        return textSurface
        # 初始化我方坦克

    def createMyTank(self):
        MainGame.my_tank = MyTank(350, 300)
        # 创建音乐对象
        music = Music('img/start.wav')
        # 调用播放音乐方法
        music.play()

    # 初始化敌方坦克，并放入到敌方列表
    def createEnemyTank(self):
        i = 0
        top = 100
        while i < MainGame.enemyTankCount:
            i += 1
            left = random.randint(0, 600)
            speed = random.randint(1, 2)

            enemy = EnemyTank(left, top, speed)
            MainGame.enemyTankList.append(enemy)

    # 循环遍历敌方坦克列表，展示敌方坦克
    def blitEnemy(self):
        for enemyTank in MainGame.enemyTankList:
            if enemyTank.live:
                enemyTank.displayTank()
                enemyTank.randMove()

                enemyTank.hitWall()
                if MainGame.my_tank and MainGame.my_tank.live:
                    enemyTank.enemyTank_hit_myTank()

                # 发射子弹
                enemyBullet = enemyTank.shot()

                # 判断敌方子弹是否我None，如果为None 则添加到敌方子弹列表

                # 将发射子弹存储到敌方子弹列表
                if enemyBullet:
                    MainGame.enmeyBulletList.append(enemyBullet)
            else:
                MainGame.enemyTankList.remove(enemyTank)  # 不活着，从敌方坦克列表移除

    # 循环遍历我方子弹列表，展示敌方子弹
    def blitEnemyBullet(self):
        for enmeyBullet in MainGame.enmeyBulletList:
            # 判断当前子弹是否活着，如果是，继续显示及移动，否则删除
            if enmeyBullet.live:
                enmeyBullet.displayBullet()
                # 调用子弹的移动
                enmeyBullet.move()
                enmeyBullet.enemyBullet_hit_myTank()
                # 敌方子弹是否与墙壁碰撞
                enmeyBullet.hitWall()
            else:
                MainGame.enmeyBulletList.remove(enmeyBullet)

    # 循环遍历显示我方子弹的显示
    def blitMyBullet(self):
        for bullet in MainGame.myBulletList:
            # 判断当前子弹是否活着，如果是，继续显示及移动，否则删除
            if bullet.live:
                bullet.displayBullet()
                # 调用子弹的移动
                bullet.move()
                bullet.myBullet_hit_enemyTank()

                # 我方子弹是否与墙壁碰撞
                bullet.hitWall()
            else:
                MainGame.myBulletList.remove(bullet)

    # 循环遍历爆炸列表，展示爆炸效果
    def blitExplode(self):
        for explode in MainGame.exploadList:
            if explode.live:
                explode.displayExplode()
            else:
                MainGame.exploadList.remove(explode)

    # 初始化墙壁
    def createWall(self):
        for i in range(6):
            wall = Wall(i * 130, 220)
            MainGame.wallList.append(wall)

    # 循环遍历墙壁列表
    def blitWall(self):
        for wall in MainGame.wallList:
            if wall.live:
                wall.displayWall()
            else:
                MainGame.wallList.remove(wall)


class Tank(BaseItem):
    # 添加距离左边left 距离上边top
    def __init__(self, left, top):
        # 保存加载的图片
        self.images = {'U': pygame.image.load('img/p1tankU.gif'),
                       'R': pygame.image.load('img/p1tankR.gif'),
                       'L': pygame.image.load('img/p1tankL.gif'),
                       'D': pygame.image.load('img/p1tankD.gif'),
                       }
        # 方向
        self.direction = "U"

        # 根据当前图片的方向获取图片
        self.image = self.images[self.direction]

        # 获取图片区域
        self.rect = self.image.get_rect()

        # 设置区域left 和 top
        self.rect.left = left
        self.rect.top = top

        # 速度 决定移动的快慢
        self.speed = 10

        # 坦克移动的开关
        self.stop = True

        self.live = True

        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

    # 移动
    def move(self):
        # 移动后记录原始的坐标
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < SCREEN_WIDTH:
                self.rect.left += self.speed
        elif self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < SCREEN_HEIGHT:
                self.rect.top += self.speed

    # 射击
    def shot(self):
        return Bullet(self)

    # 检测坦克是否与墙壁发生碰撞
    def hitWall(self):
        for wall in MainGame.wallList:
            if pygame.sprite.collide_rect(self, wall):
                # 将坐标设置为移动之前的
                self.stay()

    def stay(self):
        self.rect.left = self.oldLeft
        self.rect.top = self.oldTop

    # 显示坦克的方法
    def displayTank(self):
        # 获取展示的对象
        self.image = self.images[self.direction]

        # 调用blit方法进行展示
        MainGame.window.blit(self.image, self.rect)


# 我方坦克类
class MyTank(Tank):

    def __init__(self, left, top):
        super(MyTank, self).__init__(left, top)

    # 检测我方坦克与敌方坦克发生碰撞
    def myTank_hit_enemyTank(self):
        # 循环遍历敌方坦克列表
        for enemy in MainGame.enemyTankList:
            if pygame.sprite.collide_rect(self, enemy):
                self.stay()


# 敌方坦克
class EnemyTank(Tank):
    def __init__(self, left, top, speed):
        # 调用父类初始化方法
        super(EnemyTank, self).__init__(left, top)
        # 加载图片集
        self.images = {
            'U': pygame.image.load('img/enemy1U.gif'),
            'D': pygame.image.load('img/enemy1D.gif'),
            'L': pygame.image.load('img/enemy1L.gif'),
            'R': pygame.image.load('img/enemy1R.gif')
        }

        # 方向
        self.direction = self.randDirection()
        # 根据方向获取图片
        self.image = self.images[self.direction]

        # 区域
        self.rect = self.image.get_rect()

        # 对left和top赋值
        self.rect.left = left
        self.rect.top = top
        # 速度
        self.speed = speed

        # 移动开关
        self.flag = True

        # 步数变量
        self.step = 30

    def randDirection(self):
        num = random.randint(1, 4)
        if num == 1:
            return 'U'
        elif num == 2:
            return 'D'
        elif num == 3:
            return 'L'
        elif num == 4:
            return 'R'

    # 随机移动的方法
    def randMove(self):
        # num =
        if self.step <= 0:
            self.direction = self.randDirection()
            self.step = 50
        else:
            self.move()
            self.step -= 1

    # 重写shot方法
    def shot(self):
        num = random.randint(1, 100)
        if num < 10:
            return Bullet(self)

    def enemyTank_hit_myTank(self):
        if pygame.sprite.collide_rect(self, MainGame.my_tank):
            self.stay()


class Bullet(BaseItem):

    def __init__(self, tank):
        # 加载图片
        self.image = pygame.image.load('img/enemymissile.gif')
        # 坦克的方向决定子弹的方向
        self.direction = tank.direction

        # 获取区域
        self.rect = self.image.get_rect()
        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        # 速度
        self.speed = 7
        # 用来记录子弹是否活着，子弹的状态
        self.live = True

    # 移动
    def move(self):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                # 修改子弹的状态
                self.live = False
        if self.direction == 'R':
            if self.rect.left + self.rect.width < SCREEN_WIDTH:
                self.rect.left += self.speed
            else:
                # 修改子弹的状态
                self.live = False
        if self.direction == 'U':
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                # 修改子弹的状态
                self.live = False
        if self.direction == 'D':
            if self.rect.top + self.rect.height < SCREEN_HEIGHT:
                self.rect.top += self.speed
            else:
                # 修改子弹的状态
                self.live = False

    # 子弹是否碰撞墙壁
    def hitWall(self):
        # 循环遍历墙壁列表
        for wall in MainGame.wallList:
            if pygame.sprite.collide_rect(self, wall):
                # 让子弹消失
                self.live = False
                # 墙壁的生命值减小
                wall.hp -= 1

                if wall.hp <= 0:
                    # 修改墙壁状态
                    wall.live = False

    # 展示子弹的方法
    def displayBullet(self):
        # 调用blit方法进行展示
        MainGame.window.blit(self.image, self.rect)

    # 我方子弹与敌方碰撞的检测
    def myBullet_hit_enemyTank(self):
        # 循环遍历敌方坦克列表，判断是否发生碰撞
        for enemyTank in MainGame.enemyTankList:
            if pygame.sprite.collide_rect(enemyTank, self):
                # 修改敌方坦克状态
                enemyTank.live = False
                self.live = False
                explod = Explode(enemyTank)
                # 创建爆炸对象，将爆炸对象添加到爆炸列表中
                MainGame.exploadList.append(explod)

    # 敌方子弹与我方子弹的碰撞
    def enemyBullet_hit_myTank(self):
        if MainGame.my_tank and MainGame.my_tank.live:
            if pygame.sprite.collide_rect(MainGame.my_tank, self):
                # 创建爆炸对象，将爆炸对象添加到爆炸列表中
                explode = Explode(MainGame.my_tank)
                # 修改敌方子弹状态和我方坦克状态
                MainGame.exploadList.append(explode)
                self.live = False
                MainGame.my_tank.live = False


class Wall:
    def __init__(self, left, top):
        self.image = pygame.image.load('img/steels.gif')
        # 获取墙壁区域
        self.rect = self.image.get_rect()

        # 设置位置left，top
        self.rect.left = left
        self.rect.top = top

        # 是否活着
        self.live = True
        # 设置生命值
        self.hp = 3

    # 展示墙壁的方法
    def displayWall(self):
        MainGame.window.blit(self.image, self.rect)


class Explode:
    def __init__(self, tank):
        # 爆炸的位置将由子弹打中坦克的位置决定
        self.rect = tank.rect
        # 加载图片集
        self.images = [
            pygame.image.load('img/blast0.gif'),
            pygame.image.load('img/blast1.gif'),
            pygame.image.load('img/blast2.gif'),
            pygame.image.load('img/blast3.gif'),
            pygame.image.load('img/blast4.gif'),
        ]

        self.step = 0
        self.image = self.images[self.step]

        # 是否活着
        self.live = True

    # 显示爆炸的效果方法
    def displayExplode(self):
        # 根据索引获取爆炸效果
        self.image = self.images[self.step]

        if self.step < len(self.images) - 1:
            self.step += 1
            # 添加到主窗口
            MainGame.window.blit(self.image, self.rect)
        else:
            self.live = False
            self.step = 0


class Music:

    def __init__(self, filename):
        print(filename)
        self.filename = filename
        # 初始化音乐混合器
        pygame.mixer.init()
        pygame.mixer.music.load(self.filename)

    # 播放音乐的方法
    def play(self):
        pygame.mixer.music.play()


if __name__ == '__main__':
    # MainGame().getTextSuface()
    MainGame().startGame()
