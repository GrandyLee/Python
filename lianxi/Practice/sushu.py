#!/usr/bin/python
# -*- coding: UTF-8 -*-
class student:
    name=''
    age=0
    __weight=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w

    def speak(self):
        print("%s 说：我%d岁。"%(self.name,self.age))

pp=student('ray',24,67)
pp.speak()

