# class Person:
#     name="阿里郎"
#
# p = Person()
# print(p.name)


class Person:
    __name="阿里郎"
    def getName(self):
        return self.__name

p = Person()
print(p.getName())

print(p._Person__name)  #伪私有
