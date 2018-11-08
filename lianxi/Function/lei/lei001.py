class Parent():
    def hello(self):
        print("正在调用父类的方法……")


class Child(Parent):
    def hello(self): # 方法重写
        print("正在调用子类的方法")
    pass


p=Parent()
p.hello()

c=Child()
c.hello()