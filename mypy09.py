# 对象（object）(oop)

# class MyClass:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(name)
#         print(age)
#
#     def update_age(self):
#         self.age = 50
#         print(self.age, '你已经不年轻了，不要在装嫩了')
#
#
# mc = MyClass('wen', 18)
# mc.update_age()
# mc.name = 'LiuLaoLao'
# print(mc.name)
# # isinstance 检查一个对象是否为一个类的实例
# print(isinstance(mc, MyClass))
# print(MyClass)

# 变量为类的属性
# 类中定义的函数叫做方法
# class Person:
#
#     def __init__(self, name):
#         self.name = name
#
#     def say_hello(self):
#         print('你好，我是', self.name)
#
#
# # 所有实例都一样 放在类对象
# # 如果属性方法是独有的 放在实例对象里面
# # 属性放在实例对象，方法放在类对象
# p1 = Person('猪八戒')
# p2 = Person('孙悟空')
# p1.say_hello()
# p2.say_hello()

# getter 和 setter （封装）
# class ReactAngle:
#     """
#         表示矩形的类
#     """
#
#     def __init__(self, width, height):
#         self.hidden_width = width
#         self.hidden_height = height
#
#     def get_width(self):
#         return self.hidden_width
#
#     def get_height(self):
#         return self.get_height
#
#     def set_width(self, width):
#         self.hidden_width = width
#
#     def set_width(self, height):
#         self.hidden_height = height
#
#     def get_area(self):
#         return self.hidden_width * self.hidden_height


# r = ReactAngle(5, 2)
# r.set_width(100)
# print(r.get_area())

# 私有属性
# class Person:
#     def __init__(self, name, age):
#         # 不推荐
#         # self.__name = name
#         # self.__age = age
#
#         # 推荐（一般为私有属性，没有特殊要求，不要修改）
#         self._name = name
#         self._age = age
#
#     @property  # 装饰器 （ 将get方法转换为对象属性 ）必须和属性名一样
#     def name(self):
#         return self._name
#
#     @name.setter  # 设置装饰器
#     def name(self, name):
#         self._name = name


# p = Person('wen', 18)
# p.name = 'son'
# print(p.name)
# p._Person__name = 'liu'
# print(p._Person__name)


# 继承及重写
# class Animal:
#
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, name):
#         self._name = name
#
#     def run(self):
#         print('动物会跑。。。。')
#
#     def sleep(self):
#         print('动物睡觉。。。')
#
#
# class Dog(Animal):
#
#     def __init__(self, name, age):
#         super().__init__(name)  # 推荐
#         # self._name = name # 不推荐
#         # Animal.__init__(self, name) 不推荐
#         self._age = age
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def bark(self):
#         print('狗在叫。。。。。')
#
#     # 重写
#     def run(self):
#         print('旺旺。。。。。。')
#
#
# # issubclass() 检查一个类是否为另一个类的子类
# # isinstance() 一个类是否为一个实例的对象
# d = Dog('旺财', 18)
# print(isinstance(d, Dog))
# print(issubclass(Dog, Animal))
# print(d.name)
# print(d.age)
# d.run()

# 多重继承
# class A:
#     def test(self):
#         print('A')
#
#
# class B:
#     def test(self):
#         print('B')
#
#
# class C(A, B):
#     pass
#
#
# # c.txt 的父类
# print(C.__bases__)  # 查看多个父类
# print(C.__base__)  # 查看单个父类


# 多态
# class A:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, name):
#         self._name = name
#
#
# class B:
#     def __init__(self, name):
#         self._name = name
#
#     def __len__(self):
#         return 10
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.setter
#     def name(self, name):
#         self._name = name
#
#
# a = A('送悟空')
# b = B('猪八戒')
#
#
# # 定义一个函数
# def say_hello(obj):
#     print('你好 %s' % obj.name)
#
#
# # 违反了多态
# def say_hello2(obj):
#     if isinstance(obj, A):
#         print('你好 %s' % obj.name)
#
#
# say_hello(a)
# print(len(b))
# say_hello(b)

# class A:
#     count = 0
#
#     def test(self):
#         print('A', self)
#
#     # 类方法 类内部@classmethod来修饰的 第一个参数为cls
#     @classmethod
#     def test2(cls):
#         print('他是一个类方法', cls)
#
#     # 静态方法 用staticmethod来修饰的
#     @staticmethod  # 可以通过类和实例调用
#     def test3():
#         print('他是一个静态方法')
#
#
# a = A()
#
# # 实例属性 只支持实例对象进行修改和访问
# a.count = 10
# a.test()  # 实例方法 类中定义，以self为第一个参数 可以通过类和实例调用
# a.test2()
#
# # 类属性
# A.count = 100
# A.test(A)
# A.test2()
#
# print(A.count)
# print(a.count)

# 垃圾回收 就是从内存中删除 有自动垃圾回收机制
# class A:
#     def __init__(self):
#         self.name = 'name'
#
#     # 对象再被垃圾回收前调用
#     def __del__(self):
#         print('对象被删除了', self)
#
#
# a = A()
# print(a.name)
# a = None  # 没有任何对象对A()进行引用，他就是垃圾 垃圾太多影响性能
#
# # 程序结束后，所有对象都会被回收
# input('回车键退出')


# 特殊方法 （魔法方法）以双下划线开始结束 特殊方法不需要手动调用 特殊情况下 自动调用
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 讲对象转换为字符串的时候调用 可以用来指定对象转换为字符串的结果
    def __str__(self):
        return 'Person [name: %s ,age: %d]' % (self.name, self.age)

    # 对当前对象使用repr时调用 在交互模式下输出的结果
    def __repr__(self):
        return 'Hello'

    # 大于 other 与当前对象比较的另一个对象
    def __gt__(self, other):
        return self.age > other.age

    # 长度
    def __len__(self):
        return 10

    # 转换为bool值是否为 True
    def __bool__(self):
        return self.age > 17

    def __add__(self, other):
        return self.age + other.age


p1 = Person('wen', 16)
p2 = Person('xxx', 20)
print(p1)
print(p2)
print(p1 > p2)
print(p2 > p1)
print(len(p1))
print(bool(p1))
if p1:
    print(p1.name, '已经成年了')
else:
    print(p1.name, '还未成年')

print(p1 + p2)
