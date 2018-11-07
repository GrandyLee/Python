def MyFirstFunction():
    print("这是我的第一个函数！")
    print("我很激动！")
    print("感谢大使官邸！")

def MySecondFunction(name):
    print(name+"，我爱你！")

def saysome(name,words):
    print(name+'->'+words)

MyFirstFunction()

MySecondFunction("樊妮")

saysome('lwx','赶紧看看')

saysome(words='gasfs',name = 'lwx')


def test(*params):
    print('参数长度是：',len(params));
    print('第二个参数是：',params[1])

test(1,'李维新',3,5,6,'er')

