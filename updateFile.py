import xml.dom.minidom as xml
import os


def readFile(parent, parent_type, parent_value, child):
    """
        读取xml文档
       :type parent -- xml中的父节点名称(要处理的)
       :type parent_type -- 父类节点属性
       :type parent_value -- 父类节点属性值
       :type child -- 子节点名称
    """
    arr = []

    # 打开xml文档
    dom = xml.parse('arrays.xml')

    # 得到文档元素对象
    root = dom.documentElement

    nodeList = root.getElementsByTagName(parent)

    for node in nodeList:
        if node.getAttribute(parent_type) == parent_value:
            node_name = node.getElementsByTagName(child)
            i = 0
            while i < len(node_name):
                value = node_name[i].childNodes[0].nodeValue
                arr.append(value)
                i += 1

    return arr


def update(namelist):
    """
    :type namelist: object
    """
    path = 'E:/python/emoji/'

    filename_list = os.listdir(path)

    i = 0

    for name in namelist:
        for file in filename_list:
            if name in file:
                old_name = path + file
                new_name = path + str(i) + '.' + file.split(".")[1]
                i += 1
                try:
                    os.rename(old_name, new_name)
                except BaseException as e:
                    print(e)

                break


if __name__ == '__main__':
    namelist = readFile('string-array', 'name', 'emoji_filter', 'item')
    update(namelist)
    # path = 'E:/python/emoji/'
    #
    # old_name = path + '[困]@2x.png'
    # new_name = path + '80.png'
    # os.rename(old_name, new_name)
