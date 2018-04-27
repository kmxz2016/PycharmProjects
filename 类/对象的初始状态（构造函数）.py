class Person(object):
    # name = ""
    # age = 0
    # height = 0
    # weight= 0
    def run (self):
        print("run")
    def eat (self,food):
        print("eat", food)
    def __init__(self,name,age,height,weight):
        # print(name,age,height,weight)
        #这里定义属性
        self.name =name
        self.age = age
        self.height = height
        self.weight = weight

"""
构造函数：__init__()   在使用类创建对象时自动调用
如果不写出构造函数，默认会自动添加一个空的构造函数
"""


per = Person("hamei",20,173,74)
print(per.name,per.age,per.height,per.weight)

# per.run()
# print(per.run)

per1 = Person("wanghao",26,183,78)
print(per1.name,per1.age,per1.height,per1.weight)