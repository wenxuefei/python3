def compare(file1, file2, newFile):
    """
    :param file1: 对比文件1
    :param file2: 对比文件2
    :param newFile: 创建查缉内容文件
    :return:
    """
    list1 = set()
    list2 = set()
    try:
        with open(file1, "r", encoding="utf-8") as f, open(file2, "r", encoding="utf-8") as f1:

            while True:
                str1 = f.readline()
                str2 = f1.readline()

                list1.add(str1.strip('\n').strip('\t'))
                list2.add(str2.strip('\n').strip('\t'))

                if not str1 and not str2:
                    break

        with open(newFile, 'w', encoding="utf-8") as f3:
            s3 = list2 - list1
            for i in s3:
                f3.write(i + '\n')
            print("程序执行完成。。。。。")
    except BaseException as e:
        print(e)
        print("捕捉异常，程序执行中断")


if __name__ == '__main__':
    compare("snow.txt", "Test.txt", "33.txt")
