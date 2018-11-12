def jiecheng(m,n):
    re=0
    for i in range(m,n+1):
        # print(i,"我是数字阶乘数")
        sum1 = 1
        for j in range(1,i+1):
            # print(j,"我是要去乘的数")
            sum1*=j
            # print(sum1,'我是每个积')
            if j==i:
                print(j,"的阶乘是：",sum1)
        re=re+sum1
    print('该数字的阶乘和是：',re)
def shuru():
    start_num=input("请输入要计算的阶乘的开始数字：")
    stop_num=input("请输入要计算的阶乘的结束数字：")
    if stop_num<start_num:
        print("输入错误！")
    elif ((int(start_num)<1) or (int(stop_num)>200)):
        print("请输入1到200的数字！")
    else:
        jiecheng(int(start_num),int(stop_num))

if __name__ == '__main__':
    shuru()