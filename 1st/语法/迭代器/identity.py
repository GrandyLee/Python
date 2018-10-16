# -*- coding: UTF-8 -*-
str1 = 'liweixinfanni'
iter1 = iter(str1)
print(str1)
# for i in iter1:
#     print(i)
# print('************')
# for x in str1:
#     print(x)
while True:
    try:
        print( next (iter1))
    except StopAsyncIteration:
        break
