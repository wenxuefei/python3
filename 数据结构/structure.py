import timeit


#
#
# # 测试append和insert执行速度
# def append_test():
#     li = []
#     for i in range(10000):
#         li.append(i)
#
#
# def insert_test():
#     li = []
#     for i in range(10000):
#         li.insert(0, i)
#
#
# # 测试执行时间
# append_time = timeit.Timer('append_test()', 'from __main__ import append_test')
# print('append插入执行时间：', append_time.timeit(1000))
#
# insert_time = timeit.Timer('insert_test()', 'from __main__ import insert_test')
# print('insert插入执行时间：', insert_time.timeit(1000))

class Node:
    def __init__(self, elem):
        # elem 指数据元素
        self.elem = elem

        # 指向下一个节点的链接域
        self.next = None


# 构造单向链表类
class SingleLinkList:
    def __init__(self, node=None):
        # 判断node是否为空
        if node is not None:
            headNode = Node(node)
            self.__head = headNode
        else:
            self.__head = node

    # 在头部添加元素
    def add(self, item):
        node = Node(item)

        # 将新节点的链接域next指向头节点
        node.next = self.__head
        # 将链表的头__head指向新节点
        self.__head = node

    # 在链表尾部添加元素
    def append(self, item):
        # 将传入的值构造成节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            curNode = self.__head
            while curNode.next is not None:
                curNode = curNode.next

            # 修改节点指向 最后一个节点的next指向node
            curNode.next = node

    # 在指定位置添加元素
    def insert(self, pos, item):
        # 如果小于等于0 则插入到头部
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            count = 0
            pre_node = self.__head
            while count < pos - 1:
                count += 1
                pre_node = pre_node.next
            # 修改指向
            # 将前一个节点next指向插入位置节点
            node.next = pre_node.next
            # 将插入位置的前一个节点的next指向新节点
            pre_node.next = node

        # 如果大于链表长度 则插入到尾部

    # 删除元素
    def delete(self, item):
        curNode = self.__head
        preNode = None
        while curNode is not None:
            if curNode.elem == item:
                if preNode is None:
                    self.__head = curNode.next
                else:
                    preNode.next = curNode.next
                break
            else:
                preNode = curNode
                curNode = curNode.next

    # 查找节点是否存在
    def search(self, item):
        curNode = self.__head
        while curNode is not None:
            if curNode.elem == item:
                print("找到了！！！！！")
                print(curNode.elem, end='\t')
                return True
            else:
                curNode = curNode.next

        return False

    def travel(self):
        curNode = self.__head
        while curNode is not None:
            print(curNode.elem, end='\t')
            curNode = curNode.next
        print("")

    # 判断单向链表是否为空
    def is_empty(self):
        # if self.__head == None:
        #     return  True
        # else:
        #     return False

        return self.__head is None

    # 链表的长度
    def length(self):
        count = 0
        curNode = self.__head
        while curNode is not None:
            count += 1
            curNode = curNode.next

        return count


# 双向链表节点
class Node2:
    def __init__(self, elem):
        self.item = elem
        self.next = None
        self.pre = None


# 构造双向链表类
class DoubleLinkList:
    def __init__(self, node=None):
        # 判断node 是否为空
        if node is not None:
            headNode = Node(node)
            self.__head = headNode
        else:
            self.__head = node

    def add(self, item):
        node = Node(item)
        # 判断是否为空链表
        if self.is_empty():
            self.__head = node
        else:

            # 将新节点的链接域next指向头节点
            node.next = self.__head
            # 将链表的头__head指向新节点
            self.__head.pre = node
            self.__head = node

    def append(self, item):
        # 将传入的值构造成节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            curNode = self.__head
            while curNode.next is not None:
                curNode = curNode.next

            # 修改节点指向 最后一个节点的next指向node
            curNode.next = node
            # 将node节点前驱指向当前节点
            node.pre = node

    def insert(self, pos, item):
        # 如果小于等于0 则插入到头部
        if pos <= 0:
            self.add(item)

        # 如果大于链表长度 则插入到尾部
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = Node(item)
            count = 0
            curNode = self.__head
            while count < pos - 1:
                count += 1
                curNode = curNode.next
            # 修改指向
            # 将node节点前驱指向当前节点
            node.pre = curNode
            # 将node节点后驱指向当前节点的下一个节点
            node.next = curNode.next
            # 将当前节点的下一个节点的前驱指向node节点
            curNode.next.pre = node
            # 将当前节点后继指向当前节点
            curNode.next = node

    def delete(self, item):
        curNode = self.__head
        while curNode is not None:
            if curNode.elem == item:
                if curNode == self.__head:
                    self.__head = curNode.next
                    if curNode.next:
                        curNode.next.pre = None
                else:
                    curNode.pre.next = curNode.next
                    if curNode.next:
                        curNode.next.pre = curNode.pre
                break
            else:
                curNode = curNode.next

    def length(self):
        count = 0
        curNode = self.__head
        while curNode is not None:
            count += 1
            curNode = curNode.next

        return count

    def search(self, item):
        curNode = self.__head
        while curNode is not None:
            if curNode.elem == item:
                print("找到了！！！！！")
                print(curNode.elem, end='\t')
                return True
            else:
                curNode = curNode.next

        return False

    def travel(self):
        curNode = self.__head
        while curNode is not None:
            print(curNode.elem, end='\t')
            curNode = curNode.next
        print("")

    # 判断链表是否为空
    def is_empty(self):
        # if self.__head == None:
        #     return  True
        # else:
        #     return False

        return self.__head is None


# 栈
class Stack:
    def __init__(self):
        self.__list = []

    # 压栈
    def push(self, item):
        self.__list.append(item)

    # 弹出元素
    def pop(self):
        return self.__list.pop()

    # 返回栈顶元素
    def peek(self):
        return self.__list[len(self.__list) - 1]

    # 判断栈是否为空
    def is_empty(self):
        return self.__list == []

    # 计算栈的大小
    def size(self):
        return len(self.__list)


# 队列
class Queue:
    def __init__(self):
        self.__list = []

    # 进队
    def enqueue(self, item):
        # self.__list.append(item)
        self.__list.insert(0, item)

    # 出队
    def dequeue(self):
        # return self.__list.pop(0)
        return self.__list.pop()

    # 判断队列是否为空
    def is_empty(self):
        return self.__list == []

    # 计算队列的大小
    def size(self):
        return len(self.__list)


# 定义二叉树的节点
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None


class Tree:
    def __init__(self):
        self.root = None

    # 添加节点
    def add(self, elem):
        # 创建节点
        node = Node(elem)
        if self.root is None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                curNode = queue.pop(0)
                if curNode.lchild is None:
                    curNode.lchild = node
                    return
                else:
                    queue.append(curNode.lchild)
                if curNode.rchild is None:
                    curNode.rchild = node
                    return
                else:
                    queue.append(curNode.rchild)

    # 广度优先遍历
    def travel(self):
        queue = []
        # 判断根节点是否存在
        if self.root is None:
            return
        else:
            queue.append(self.root)
        while queue:
            curNode = queue.pop(0)
            print(curNode.elem, end='\t')
            if curNode.lchild is not None:
                queue.append(curNode.lchild)
            if curNode.rchild is not None:
                queue.append(curNode.rchild)
        print()

    # 先序遍历  根  左  右 0 1 3 7 8 4 9 2 5 6
    def preOrder(self, root):
        if root is None:
            return
        else:
            print(root.elem, end='\t')
            self.preOrder(root.lchild)
            self.preOrder(root.rchild)

    # 中序遍历 左  根  右  7 3 8 1 9 4  0 5 2 6
    def inOrder(self, root):
        if root is None:
            return
        else:
            self.inOrder(root.lchild)
            print(root.elem, end='\t')
            self.inOrder(root.rchild)

    # 后序遍历  左  右  根 7 8 3 9 4 1 5 6 2 0
    def lastOrder(self, root):
        if root is None:
            return
        else:
            self.lastOrder(root.lchild)
            self.lastOrder(root.rchild)
            print(root.elem, end='\t')


if __name__ == '__main__':
    # # 初始化一个元素值为20 的单向链表
    # singLinkList1 = SingleLinkList(20)
    # singLinkList = SingleLinkList()
    #
    # print(singLinkList)
    # print(singLinkList1)
    # print('是否空链表：', singLinkList.is_empty())
    # print('链表长度：', singLinkList1.length())
    #
    # print("---------头部插入----------------")
    # singLinkList1.add(1)
    # singLinkList1.add(2)
    # singLinkList1.add(3)
    #
    # print("---------尾部插入----------------")
    # singLinkList.append(44)
    # singLinkList1.append(44)
    #
    # print("---------指定位置插入插入----------------")
    # # singLinkList.insert(4, 33)
    # singLinkList1.insert(2, 100)
    #
    # print("---------删除节点----------------")
    # singLinkList.delete(44)
    # singLinkList1.delete(100)
    #
    # print("---------遍历单链表----------------")
    # singLinkList.travel()
    # singLinkList1.travel()
    #
    # print("---------查找----------------")
    # singLinkList1.search(20)
    # singLinkList1.search(30)

    # doubleLinkList = DoubleLinkList()
    # doubleLinkList.add(11)
    # doubleLinkList.add(22)
    # doubleLinkList.add(33)
    # doubleLinkList.append(44)
    # doubleLinkList.append(55)
    # doubleLinkList.insert(3, 88)
    # doubleLinkList.delete(11)
    # doubleLinkList.delete(55)
    # doubleLinkList.travel()

    # stack = Stack()
    # print('是否空栈吗', stack.is_empty())
    # # 压栈
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # stack.push(4)
    # print('是否空栈吗', stack.is_empty())
    # print('栈的长度：', stack.size())
    # # 弹出
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())

    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    # 判断队列是否空
    print(queue.is_empty())
    print('队列大小', queue.size())
    print('-----出队---------')
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
