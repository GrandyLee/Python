import random
secret=random.randint(1,10)
print(secret)
print("猜数字游戏")
temp=input("不妨猜猜我心中的数字：")
guess=int(temp)
while guess!=secret:
    temp=input('哎呀，猜错了，请重新输入：')
    guess=int(temp)
    if guess==secret:
        print('猜对了')
    else:
        if guess>secret:
            print('大了，大了')
        else:
            print('小了，小了')
print('游戏结束！')