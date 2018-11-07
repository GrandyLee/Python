import math
import time
result = []  # 最终结果
start1=input("请输入起始数字：")
end1=input("请输入结束数字：")
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

start = time.clock()
print("start:" )
for x in range(int(start1),(int(end1)+1)):
    # print(x)
    if is_prime(x) is True:
        result.append(x)

print(result)

end = time.clock()
times = ''.join("%f s" % (end - start))
print("end!\n耗时：", times)