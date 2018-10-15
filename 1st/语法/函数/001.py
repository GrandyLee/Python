# -*- coding: UTF-8 -*-
a=3.4
def sum(num1,num2):
	# 两数之和
	if not (isinstance (num1,(int ,float)) and isinstance (num2,(int ,float))):
		raise TypeError('参数类型错误')
	return num1+num2

print(sum(a,2))