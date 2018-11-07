class Turtle:
    color="green"
    weight=40
    legs=4
    shell=True
    mouth='大嘴'

    #方法
    def climb(self):
        print("我在努力的爬啊爬！")

    def run(self):
        print("我整下飞象前方")

    def bite(self):
        print("咬死你，要死你")

    def eat(self):
        print("youzhiyouhe")

    def sleep(self):
        print("还可以睡觉")

tt=Turtle()

# print(tt)

tt.bite()
tt.climb()
tt.eat()
