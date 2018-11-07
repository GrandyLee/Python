number=input("请输入要录入的学生人数：")
for i in range(int(number)):
    temp=input("请输入第"+str(i+1)+"个学生的分数：")
    score= int(temp)

    if (score<0) or (score>100):
        print("输入错误！")
    elif (score<60):
        print("你的成绩是：D")
    elif(score<80):
        print("你的成绩是：C")
    elif(score<90):
        print("你的成绩是：B")
    else:
        print("你的成绩是:A")
print("录入完毕！")