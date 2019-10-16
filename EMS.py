print('-' * 20, '欢迎使用员工管理系统', '-' * 20)
employee = ['\t猪八戒\t30\t男\t高老庄']
while True:
    print('请选择你要做的操作：')
    print('\t\t1、查询员工')
    print('\t\t2、添加员工')
    print('\t\t3、删除员工')
    print('\t\t4、推出系统')
    print('-' * 62)
    select = input('请选择要做的操作：')
    if select == '1':
        print('\t序号\t姓名\t年龄\t性别\t住址')
        n = 1
        for emp in employee:
            print(f'\t{n}\t{emp}')
            n += 1
        if len(employee) == 0:
            print('\t\t\t暂无员工信息！\t')
        pass
    elif select == '2':
        # item = {}
        # item.num = input('请输入员工序号：')
        # item.name = input('请输入员工姓名：')
        # item.age = input('请输入员工年龄：')
        # item.sex = input('请输入员工性别：')
        # item.address = input('请输入员工住址：')
        # list.append()
        name = input('请输入员工姓名：')
        age = input('请输入员工年龄：')
        sex = input('请输入员工性别：')
        address = input('请输入员工住址：')
        emp = f'{name}\t{age}\t{sex}\t{address}'
        print('-' * 62)
        print('您确认要添加以下员工吗？')
        print('姓名\t年龄\t性别\t住址')
        print(emp)
        confirm = input('您确认要添加此员工吗? 是否确认该操作[y/n]:')
        if confirm == 'y' or confirm == 'yes':
            employee.append(f'\t{emp}')
            print('添加成功！！！')
        else:
            print('添加已取消！！')
        pass
    elif select == '3':
        num = int(input('请输入要删除的员工序号：'))
        if num > len(employee) or num <= 0:
            print('输入有误，请重新操作！')
            continue
        print('您确认要删除以下员工吗？')
        print('\t姓名\t年龄\t性别\t住址')
        print(employee[num - 1])
        confirm = input('您确认要删除此员工吗? 是否确认该操作[y/n]:')
        if confirm == 'y' or confirm == 'yes':
            employee.pop(num - 1)
            print('删除成功！！！')
        else:
            print('删除已取消！！')
    elif select == '4':
        print('欢迎使用，再见！')
        input('点击回车键推出!')
        print('您已成功推出系统！')
        break
    else:
        print('输入错误，请重新输入！！！！')
    print('-' * 62)
