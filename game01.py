print('=' * 20, '欢迎光临《唐僧大战白骨精》', '=' * 20)
print('请选择你的身份：')
print('\t\t1唐僧')
print('\t\t2白骨精')

select = input('请选择你的身份：')
print("-" * 60)
if select == '1':
    print("恭喜你以唐僧的身份进行游戏！")
elif select == '2':
    print("你竟然选择了白骨精，太不要脸了，系统将自动分配身份，恭喜你以唐僧的身份进行游戏！")
else:
    print("你的输入有误，系统将自动分配身份，恭喜你以唐僧的身份进行游戏！")

beat = 2
life = 2

boss_beat = 60
boss_life = 60

print("你的身份是-->唐僧<--,你的攻击力是：", beat, "，生命值是：", life)
print("-" * 60)

while True:
    print("请选择你要做的操作：")
    print('\t\t1练级')
    print('\t\t2打boss')
    print('\t\t3逃跑')
    select2 = input('请选择你要做的操作：')
    print("-" * 60)
    if select2 == '1':
        beat += 2
        life += 2
        print(f"恭喜你升级了，你的攻击力升级为{beat}，你的生命值升级为{life}")
    elif select2 == '2':
        boss_life -= beat
        print("-->唐僧<--攻击了-->白骨精<--")
        if boss_life <= 0:
            print(f'-->白骨精<--收到了{beat}点伤害')
            print('恭喜你成功打败了白骨精')
            print('游戏结束')
            break
        else:
            print("-->白骨精<--攻击了-->唐僧<--")
            life -= boss_beat
            if life <= 0:
                print(f'-->唐僧<--收到了{boss_beat}点伤害')
                print('游戏结束')
                break
    elif select2 == '3':
        print('唐僧逃跑了')
    else:
        print('你的输入有误，请重新输入！')
    print("-" * 60)
