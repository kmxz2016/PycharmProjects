#python内置了map和reduce函数

# map（fn,1sd）    参数1是函数，参数2是序列
from functools import reduce

#功能：将传入的函数依次作用在序列中的每一个元素，并把结果作为新的Iterator返回

def chr2int(chr):
    return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,}[chr]
list1 = ["6","9","4","7"]
res = map(chr2int,list1)
print(list(res))

#将整数元素的序列，转为字符串类型
l = map(str,[1,4,6,7])
print(list(l))
# reduce（fn,1sd）    参数1是函数，参数2是序列
#功能：一个函数作用在序列上，这个函数必须接受两个参数，reduce把结果继续和序列的下一个元素累计运算


#求一个序列的和
list2 = [2,5,7,8,9]

def mySum(x,y):
    return x+y
r = reduce(mySum,list2)
print("r=",r)

#将字符串转成对应字面量数字
def str2int(str):
    def fc(x,y):
        return x*10+y
    def fs(chr):
        return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, }[chr]
    return reduce(fc,map(fs,list(str)))

a = str2int("14567")
print(a)
print(type(a))