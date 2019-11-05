import time
import asyncio

# yield 的使用
# def foo():
#     print('starting')
#     while True:
#         res = yield 4
#         print('res:', res)
#
#
# """
# 在函数使用yield,则该函数便成为了一个生成器
# yield:
# 1.当成return 程序返回
# 2.当成生成器
# """
# g = foo()
# print(next(g))
# print('*'*20)
# print(next(g))

# yield简单实现协程
# def A():
#     while True:
#         print('----A----')
#         yield
#         time.sleep(0.5)
#
#
# def B(a):
#     while True:
#         print('----B----')
#         a.__next__()
#         time.sleep(0.5)
#
#
# a = A()
# B(a)

# send 发送数据
# def foo():
#     print('starting')
#     while True:
#         res = yield 4
#         print('res:', res)
#
#
# g = foo()
# print(next(g))
# print(next(g))
# print(g.send(10))

# yield 实现消费者生产者

# def produce(a):
#     for i in range(1, 11):
#         print('生产者生产产品：%d' % i)
#         a.send(str(i))
#
#
# def consumer():
#     while True:
#         res = yield
#         print('消费者消费产品：', res)
#
#
# c = consumer()  # 生成器对象
# next(c)  # 在一个生成器函数未启动之前，是不能传递数值进去。必须先传递一个None进去或者调用一次next(c)方法，才能进行传值操作
# produce(c)


# 同步和异步
"""
同步：先执行第一个事务，如果遇到阻塞，会一直等待，知道第一个事务执行完毕，才会执行第二个
异步：与同步是相对的，指执行第一个事务遇到阻塞，会直接执行第二个事务，不会等待 通过状态，通知，回调来调用处理结果
"""


# now = lambda: time.time()
# print(now())
#
#
# def foo():
#     time.sleep(1)
#
#
# start = now()
# for i in range(5):
#     foo()
#
# print('同步所花费的时间：', (now() - start))


# 协程实现异步
# async def foo():
#     asyncio.sleep(1)
#
#
# now = lambda: time.time()
# loop = asyncio.get_event_loop()
# start = now()
# for i in range(5):
#     loop.run_until_complete(foo())
# print('异步所花费的时间：', (now() - start))

# 定义协程
# 使用async来修饰一个函数，则该函数就成为一个协程对象
# now = lambda: time.time()
#
#
# async def do_work(x):
#     print('waiting:', x)
#
#
# # 调用协程
# start = now()
# # 创建事件循环
# loop = asyncio.get_event_loop()
# # 将协程对象加入到事件循环中
# loop.run_until_complete(do_work(3))
# print('异步所花费的时间：', (now() - start))

# 创建task
# async def do_work(x):
#     print('waiting:', x)
#
#
# # 获取协程对象
# coroutine = do_work(3)
# # 创建事件循环
# loop = asyncio.get_event_loop()
# # 创建任务
# # task = asyncio.ensure_future(coroutine)
# task = loop.create_task(coroutine)
# print(task)
# # 将协程对象加入到事件循环中
# loop.run_until_complete(task)
# print(task)
# print('task是否为future的子类', isinstance(task, asyncio.Future))

# 回调
# async def do_work(x):
#     print('waiting:', x)
#     return 'Done after {}s'.format(x)
#
#
# # 定义回调函数
# def callback(future):
#     print('Callback:', future.result())
#
#
# # 获取协程对象
# coroutine = do_work(3)
# # 创建事件循环
# loop = asyncio.get_event_loop()
# # 创建任务
# task = loop.create_task(coroutine)
# # 给任务添加绑定函数
# # task.add_done_callback(callback)
# # 将协程对象加入到事件循环中
# loop.run_until_complete(task)
# # 直接调用task中的result来获取返回结果
# print('直接获取结果：', task.result())

# await
# now = lambda: time.time()
# async def do_work(x):
#     print('waiting:', x)
#     await asyncio.sleep(x)
#     return 'Done after {}s'.format(x)
# start = now()
# # 获取协程对象
# coroutine = do_work(3)
# # 创建事件循环
# loop = asyncio.get_event_loop()
# # 创建任务
# task = loop.create_task(coroutine)
# # 给任务添加绑定函数
# # task.add_done_callback(callback)
# # 将协程对象加入到事件循环中
# loop.run_until_complete(task)
# # 直接调用task中的result来获取返回结果
# print('直接获取结果：', task.result())
# print('TIME：', (now() - start))

# # 并发和并行
# async def do_work(x):
#     print('waiting:', x)
#     await asyncio.sleep(x)
#     return 'Done after {}s'.format(x)
#
#
# now = lambda: time.time()
# start = now()
# # 获取协程对象
# coroutine1 = do_work(1)
# coroutine2 = do_work(2)
# coroutine3 = do_work(3)
#
# # 创建任务
# tasks = [
#     asyncio.ensure_future(coroutine1),
#     asyncio.ensure_future(coroutine2),
#     asyncio.ensure_future(coroutine3),
# ]
#
# # 将协程对象加入到事件循环中
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
#
# # 获取返回的结果
# for task in tasks:
#     print('Task result:', task.result())
#
# print('TIME：', (now() - start))


# 协程的嵌套
# async def do_work(x):
#     print('waiting:', x)
#     await asyncio.sleep(x)
#     return 'Done after {}s'.format(x)
#
#
# async def main():
#     # 创建多个协程对象
#     # 封装任务列表
#     coroutine1 = do_work(1)
#     coroutine2 = do_work(2)
#     coroutine3 = do_work(3)
#
#     tasks = [
#         asyncio.ensure_future(coroutine1),
#         asyncio.ensure_future(coroutine2),
#         asyncio.ensure_future(coroutine3),
#     ]
#     # 获取返回结果的方式（方式一）
#     # dones, pendings = await asyncio.wait(tasks)
#     # for task in dones:
#     #     print('Task result:', task.result())
#     # 获取返回结果的方式（方式二）
#     # results = await asyncio.gather(*tasks)
#     # for result in results:
#     #     print('Task result:', result)
#     # 获取返回结果的方式（方式三）
#     # return await asyncio.gather(*tasks)
#     # print('TIME：', (now() - start))
#     # 获取返回结果的方式（方式四）
#     # return await asyncio.wait(tasks)
#     # 获取返回结果的方式（方式五）
#     for task in asyncio.as_completed(tasks):
#         result = await task
#         print('Task result:{}'.format(result))
#
#
# now = lambda: time.time()
# start = now()
# # 将协程对象加入到事件循环中
# loop = asyncio.get_event_loop()
# # loop.run_until_complete(main())
# # 获取返回结果的方式（方式三）
# # results = loop.run_until_complete(main())
# # for result in results:
# #     print('Task result:', result)
# # 获取返回结果的方式（方式四）
# # dones,pendings = loop.run_until_complete(main())
# # for task in dones:
# #     print('Task result:', task.result())
# # 获取返回结果的方式（方式五）
# loop.run_until_complete(main())
# print('TIME：', (now() - start))


# 协程停止（方式一）
# async def do_work(x):
#     print('waiting:', x)
#     await asyncio.sleep(x)
#     return 'Done after {}s'.format(x)
#
#
# # 创建多个协程对象
# # 封装任务列表
# coroutine1 = do_work(1)
# coroutine2 = do_work(2)
# coroutine3 = do_work(3)
#
# tasks = [
#     asyncio.ensure_future(coroutine1),
#     asyncio.ensure_future(coroutine2),
#     asyncio.ensure_future(coroutine3),
# ]
#
# now = lambda: time.time()
# start = now()
# # 将协程对象加入到事件循环中
# loop = asyncio.get_event_loop()
# try:
#     loop.run_until_complete(asyncio.wait(tasks))
# except KeyboardInterrupt as e:
#     # 获取事件循环中所有任务列表
#     print(asyncio.Task.all_tasks())
#     for task in asyncio.Task.all_tasks():
#         print(task.cancel())  # 如果返回的True代表当前任务取消成功
#     loop.stop()
#     loop.run_forever()
# finally:
#     loop.close()
# print('TIME：', (now() - start))

# 协程停止（方式二）
async def do_work(x):
    print('waiting:', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


async def main():
    # 创建多个协程对象
    # 封装任务列表
    coroutine1 = do_work(1)
    coroutine2 = do_work(2)
    coroutine3 = do_work(3)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3),
    ]

    dones, pendings = await asyncio.wait(tasks)
    for t in dones:
        print('Task result:',t.result())


now = lambda: time.time()
start = now()
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(main())
try:
    loop.run_until_complete(task)
except KeyboardInterrupt as e:
    # 获取事件循环中所有任务列表
    print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()
print('TIME：', (now() - start))
