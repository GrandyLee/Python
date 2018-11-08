import random as r

class Fish():
    def __init__(self):
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
    def move(self):
        self.x-=1
        print("我的位置时：",self.x,self.y)

class GoldFish(Fish):
    print("我是金鱼")
    pass

class Carp(Fish):
    def color(self):
        print("我是蓝色的")


class Salmon(Fish):
    pass

class Shark(Fish):
    # def __init__(self):
    #     Fish.__init__(self)
    #     print("我是鲨鱼")
    #     self.hungry = True

    def __init__(self):
        super().__init__()
        print("我是鲨鱼")
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有的吃^_^")
            self.hungry=False
        else:
            print("太撑了，吃不下了")


gold=GoldFish()
gold.move()

shark=Shark()
shark.move()


