result1 = 0
result2 = 0
i = 0
while i <= 100 :
    if i % 2 == 0:
        print(i)
        result1 += i
    else:
        pass
        print(i)
        result2 += i
    i +=1
# print("0~100偶数和为 %d", end="奇数和为 %d" % (result1 result2))
# print("0~100偶数和为%d",end="" % (result1))
print("0~100偶数和为%d" % (result1))
print("0~100奇数和为%d" % (result2))