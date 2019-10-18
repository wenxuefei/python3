import time


# start_time = time.time()
# 一般思路
# for a in range(1001):
#     for b in range(1001):
#         for c in range(1001):
#             if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
#                 print("a,b,c", a, b, c)


# 优化
# for a in range(1001):
#     for b in range(1001):
#         c = 1000 - a - b
#         if a ** 2 + b ** 2 == c ** 2:
#             print("a,b,c", a, b, c)
# end_time = time.time()

# print("所用时间：", (end_time - start_time))

# 冒泡排序
def bubble_sort(alist):
    n = len(alist)
    for j in range(n - 1):
        # j 表示每次遍历需要比较的次数，是逐渐减小的

        for i in range(n - 1 - j):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


# 选择排序法
def selection_sort(alist):
    n = len(alist)
    for j in range(n - 1):
        # 记录最小值位置
        minIndex = j
        # 从j+1 位置到末尾选择出最小数据
        for x in range(j + 1, n):
            if alist[x] < alist[minIndex]:
                minIndex = x
        # 如果悬着出的数据不再正确位置，进行交换
        if minIndex != j:
            alist[j], alist[minIndex] = alist[minIndex], alist[j]


# 插入排序
def insert_sort(alist):
    n = len((alist))
    for j in range(1, n):
        i = j
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            else:
                break
            i -= 1


# 快速排序
def quick_sort(alist, start, end):
    if start >= end:
        return

    # 设定起始元素寻找位置的基准元素
    mid = alist[start]

    # low 为序列左边的由左向右移动的游标
    low = start

    # high 为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果 low 与 high  为重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1

        # 将 high 指向的元素放到 low 的位置上
        alist[low] = alist[high]

        # 如果 low 与 high 未重合，low 指向的元素比基准元素小，则 low 向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将 low 指向的元素放到 high 的位置上
        alist[high] = alist[low]

        # 退出循环后，low 与 high 重合，此时所指位置为基准元素的正确位置
        # 将基准元素放到该位置

        alist[low] = mid

        # 对基准元素左边的子序列进行快速排序
        quick_sort(alist, start, low - 1)
        # 对基准元素右边的子序列进行快速排序
        quick_sort(alist, low + 1, end)


# 归并排序
def merge_sort(alist):
    if len(alist) <= 1:
        return alist

    # 二分分解
    num = len(alist) // 2

    left = merge_sort(alist[:num])

    right = merge_sort(alist[num:])

    # 合并
    return merge(left, right)


def merge(left, right):
    """合并操作，将两个有序数组 left[]和 right[]合并成一个大的有序数组"""
    l, r = 0, 0
    result = []

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1

        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


# 顺序查找法
# 从 a 列表中查找值 v,如果找到则返回第一次出现的下标，否则返回-1
def sequenceSearch(a, v):
    for i in range(len(a)):
        if a[i] == v:
            return i
    return -1


# 二分查找法（非递归实现）
def binary_search(alist, item):
    first = 0
    last = len(alist) - 1
    while first <= last:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            return True
        elif alist[midpoint] > item:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return False


# 二分查找法（递归实现）
def binary_search(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binary_search(alist[:midpoint], item)
            else:
                return binary_search(alist[midpoint + 1:], item)


a = [54, 26, 93, 17, 77, 31, 44, 55, 20, 30]
# bubble_sort(a)
# selection_sort(a)
# insert_sort(a)
# quick_sort(a, 0, len(a) - 1)
index = sequenceSearch(a, 20)
print(index)
b = merge_sort(a)
print(b)
print(binary_search(a, 17))
# print(a)
