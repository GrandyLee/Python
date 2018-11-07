class Ball:
    def __init__(self,name):
        self.name=name
    # def setName(self,name):
    #     self.name=name
    def kick(self):
        print("我叫%s,该死的，谁踢我..."%self.name)


a=Ball('球A')

b=Ball('球B')

c=Ball('土豆')

a.kick()

c.kick()

b.kick()