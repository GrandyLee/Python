import time as t
class MyTimer():
    #开始计时
    def start(self):
        self.start=t.localtime()
        print("计时开始……")
     #停止计时
    def stop(self):
        self.stop=t.localtime()
        print("停止计时……")

    #内部方法计算运行时间
    def _calc(self):
        self.lasted=[]
        self.prompt="总共运行了"
