count =5
def MyFun():
    print(10)

MyFun()

print(count)


def func1():
    print("正在调用func1")
    def func2():
        print("正在调用func2")
    func2()

func1()

def fun1(x):  # 内嵌函数
    def fun2(y):
        return x*y
    return fun2

i=fun1(3)(5)

print(i)

g=lambda x,y:x+y  #lambda 表达式
print(g(2,4))


print(list(filter(None,[1,2,3,0,False])))

temp=list(filter(lambda x: x%2,range(10)))
print(temp)

w=list(map(lambda x:x*2,range(10)))
print(w)