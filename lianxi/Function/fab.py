def fab(n):
    if n<1:
        print('输入错误！')
        return -1
    elif n<3:
        return 1
    else:
        return fab(n-1)+fab(n-2)


SUM=fab(5)
print(SUM)

print(fab(-1))