from time import sleep
from time import ctime
from multiprocessing import Process, Pool, Queue, Manager
import _thread
import threading
from threading import Thread, Lock
from queue import Queue


# 进程（系统中打开的每一个应用  分配资源，调度执行线程 一个进程拥有多个线程 占用内存大），线程 （同一个应用执行不同任务 共享进程的资源 属于进程的一部分 不利于资源管理）


# 正在运行的程序叫进程

def sing():
    for i in range(3):
        print('正在唱歌%d' % i)


def dance():
    for i in range(3):
        print('正在跳舞%d' % i)


# 创建子进程并执行

def run_test():
    print('.....test........')


def run_proc(name, age, **kwargs):
    print('子进程执行中，参数name:%s,age:%d' % (name, age))
    print('字典参数kwargs：', kwargs)


def worker(interval):
    print('work start')
    sleep(interval)
    print('work end')


def clock(interval):
    for i in range(3):
        print('当前时间：{}'.format(ctime()))
        sleep(interval)


def work1(interval):
    print('执行work1')
    sleep(interval)
    print('end work1')


def work2(interval):
    print('执行work2')
    sleep(interval)
    print('end work2')


def work3(interval):
    print('执行work3')
    sleep(interval)
    print('end work3')


# 通过类创建进程
class ClockProcess(Process):
    def __init__(self, interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        print('子进程开始执行的时间：{}'.format(ctime()))
        sleep(self.interval)
        print('子进程结束的时间：{}'.format(ctime()))


num = 0


def works1():
    global num
    num += 5
    print('子进程1运行后num的值', num)


def works2():
    global num
    num += 10
    print('子进程2运行后num的值', num)


def func(msg):
    print('start:', msg)
    sleep(3)
    print('end:', msg)


def wirte(q):
    a = ['a', 'b', 'c', 'd']
    for i in a:
        print('开始写入的值:%s' % i)
        q.put(i)
        sleep(1)


def read(q):
    for i in range(q.qsize()):
        print('读取到的值：%s' % q.get())
        sleep(i)


def fun1(thread_name, delay):
    print('开始运行fun1')
    print('线程的名：%s' % thread_name)
    sleep(delay)
    print('运行fun1结束')


def fun2(thread_name, delay):
    print('开始运行fun2')
    print('线程的名：%s' % thread_name)
    sleep(delay)
    print('运行fun2结束')


def fun3(thread_name, delay):
    print('线程{0}开始运行fun3'.format(thread_name))
    sleep(delay)
    print('线程{0}结束运行fun3'.format(thread_name))


def fun4(thread_name, delay):
    print('线程{0}开始运行fun4'.format(thread_name))
    sleep(delay)
    print('线程{0}结束运行fun4'.format(thread_name))


def fun5(delay):
    print('线程{}执行fun5'.format(threading.current_thread().getName()))
    sleep(delay)
    print('线程{}执行fun5结束'.format(threading.current_thread().getName()))


def fun6(delay):
    print('线程{}执行fun6'.format(threading.current_thread().getName()))
    sleep(delay)
    print('线程{}执行fun6结束'.format(threading.current_thread().getName()))


# 通过继承创建线程
class MyThread(threading.Thread):
    # 重写父类的构造方法，其中func是线程函数，args是传入线程的参数，name是线程名称，默认线程名字Thread-1
    def __init__(self, func, name, args):
        super().__init__(target=func, name=name, args=args)

    # 重写run方法
    def run(self):
        self._target(*self._args)


# 创建互斥锁
lock = Lock()


def test1():
    global num

    for i in range(10000):
        lock.acquire()  # 上锁
        num += 1
        lock.release()  # 释放锁
    print("test1输出 num:", num)


def test2():
    global num

    for i in range(10000):
        lock.acquire()  # 上锁
        num += 1
        lock.release()  # 释放锁
    print("test2输出 num:", num)


# 创建3把互斥锁
lock1 = Lock()
lock2 = Lock()
lock3 = Lock()

# 对lock2,lock3上锁
lock2.acquire()
lock3.acquire()


class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():
                print('------task1-----')
                sleep(1)

                # 释放lock2这把锁
                lock2.release()


class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():
                print('------task2-----')
                sleep(1)

                # 释放lock3这把锁
                lock3.release()


class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print('------task3-----')
                sleep(1)

                # 释放lock1这把锁
                lock1.release()


# 生产者消费者模式
class Produce(Thread):

    def run(self):
        global q
        count = 0
        while True:
            # 判断当前队列的大小
            if q.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = '生产第' + str(count) + '个产品'
                    q.put(msg)
                    print(msg)

                sleep(0.5)


class Constumer(Thread):
    def run(self):
        global q
        while True:
            # 判断当前队列的大小
            if q.qsize() > 100:
                for i in range(10):
                    msg = self.name + '消费' + q.get()
                    print(msg)
                    sleep(1)


# 创建ThreadLocal对象（全局变量）
local = threading.local()


def process_student():
    student_name = local.name
    print('线程名：%s 学生姓名：%s' % (threading.current_thread().getName(), student_name))


def process_thread(name):
    # 将传入name的值绑定到local的name上
    local.name = name
    process_student()


if __name__ == '__main__':
    # sing()
    # dance()

    print('主进程执行')

    # 创建子进程 target接收执行的任务
    # p = Process(target=run_test)
    # p.start()
    #
    # p = Process(target=run_proc, args=('wen', 18), kwargs={'hello': 22, 'hi': 55})
    # p.start()

    # p = Process(target=worker, args=(3,))
    # p.start()
    #
    # # 调用join方法  主进程等待调用join的子进程结束
    # p.join()

    # p = Process(target=clock,args=(1,))
    # p.start()
    # # p.join()
    # print(p.pid)
    # print(p.name)
    # print(p.is_alive())

    # p1 = Process(target=work1, args=(4,))
    # p2 = Process(target=work2, args=(2,))
    # p3 = Process(target=work3, args=(3,))
    #
    # p1.start()
    # p2.start()
    # p3.start()
    #
    # p1.join()
    # p2.join()
    # p3.join()
    #
    # print(p1.name)
    # print(p2.name)
    # print(p3.name)

    # p = ClockProcess(3)
    # p.start()
    # p.join()

    # 创建进程池
    # pool = Pool(3)
    # for i in range(1, 6):
    #     msg = '任务%d' % i
    #
    #     # 阻塞（单进程）
    #     pool.apply(func, (msg,))
    #
    #     # 非阻塞
    #     # pool.apply_async(func,(msg,))
    #
    # # 如果进程池不在接收新的请求 调用close
    # pool.close()
    # pool.join()

    # # 进程之间数据是否共享
    # p1 = Process(target=works1)
    # p2 = Process(target=works2)
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()
    #
    # print('全局变量：num', num)

    # # 创建队列
    # q = Queue(3)  # 可以指定队列的大小，如果不写默认的队列是无限
    #
    # # 向队列中插入元素
    # q.put('消息1')
    # q.put('消息2')
    # q.put('消息3')
    #
    # # put 方法可选参数 block=True,timeout=1 队列已经满了 等待1s 如果还是没有空余的空间 则跑队列已满的异常
    # # 判断当前队列是否已满
    # if not q.full():
    #     q.put('消息4', block=True, timeout=1)
    #
    # # 读取并删除元素
    # # print(q.get())
    # # print(q.get())
    # # print(q.get())
    # #
    # # if not q.empty():
    # #     print(q.get(block=True, timeout=1))
    #
    # # 查看队列的大小
    # print(q.qsize())
    # for i in range(q.qsize()):
    #     print(q.get())

    # q = Queue()

    # 进程通信
    # pw = Process(target=wirte, args=(q,))
    # pr = Process(target=read, args=(q,))
    #
    # pw.start()
    # pw.join()
    # pr.start()
    # pr.join()

    # # 进程池实现通信
    # q = Manager().Queue()
    #
    # p = Pool(3)
    # p.apply(wirte, (q,))
    # p.apply(read, (q,))
    # p.close()
    # p.join()

    # _thread 创建线程
    # t = _thread.start_new_thread(fun1, ('fun1', 5))
    # t = _thread.start_new_thread(fun2, ('fun2', 2))
    #
    # sleep(7)

    # threading 创建线程
    # t1 = threading.Thread(target=fun3, args=('thread-1', 2))
    # t2 = threading.Thread(target=fun4, args=('thread-2', 3))
    #
    # t1.start()
    # t2.start()
    #
    # t1.join()
    # t2.join()

    # t1 = MyThread(fun5, 'thread-1', (2,))
    # t2 = MyThread(fun6, 'thread-1', (4,))
    #
    # t1.start()
    # t2.start()
    #
    # t1.join()
    # t2.join()

    # 线程共享全局变量
    # t1 = threading.Thread(target=test1)
    # t2 = threading.Thread(target=test2)
    #
    # t1.start()
    # t2.start()
    #
    # t1.join()
    # t2.join()

    # 线程同步
    # t1 = Task1()
    # t2 = Task2()
    # t3 = Task3()
    #
    # t1.start()
    # t2.start()
    # t3.start()

    # 生产者消费者模式
    # q = Queue()
    # p = Produce()
    # c = Constumer()
    # p.start()
    # sleep(1)
    # c.start()

    # ThreadLocal对象
    t1 = Thread(target=process_thread, args=('张三',), name='Thread-A')
    t2 = Thread(target=process_thread, args=('李四',), name='Thread-B')

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('主进程执行完')
