#!/usr/bin/python
# -*- coding: UTF-8 -*-
count=0
def hanoi(n,x,y,z):
    global count
    if n==1:
        print(x, '-->', z)
    else:
        hanoi(n - 1,x, z, y)# 将前n-1的盘子移动到y
        print(x, '-->',z)# 将n（最后一个）个盘子移动到z上
        hanoi(n-1,y,x,z)#将y上的n-1个盘子一道z上
    count += 1

n=int(input("请输入汉诺塔的层数：\n"))
hanoi(n,'X','Y','Z')
print("总共移动了：",count,"步！")