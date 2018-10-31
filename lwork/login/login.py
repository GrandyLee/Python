import requests
import json
zhuye=requests.get(url='http://jimmy.bwqa.lwork.cn') # 基本get请求
print(zhuye.status_code) #获取返回状态

baidu=requests.get(url='http://dict.baidu.com/s', params={'wd':'python'})
print(baidu.url)
print(baidu.text)