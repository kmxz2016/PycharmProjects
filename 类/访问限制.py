class Person(object):
    def run (self):
        print(self.__money)
        print("run")
    def eat (self,food):
        print("eat", food)
    def __init__(self,name,age,height,weight,money):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.__money = money #_Person__money
    #通过内部的方法去修改私有属性
    #通过自定义的方法实现对私有属性的赋值与取值
    def setMoney(self,money):
        #数据过滤
        if money < 0:
            money = 0
        self.__money = money

    def getMoney(self):
        return self.__money

per = Person("hanmeimei",20,173,74,-6)

# per.age = 10
# print(per.age)

#要使内部属性不被外部直接访问,在属性前加“__”,在Python前加两个下划线，那属性则变为私有属性

# per.__money = 0
# print(per.__money)

# per.b = 60
# print(per.b)
# per.run()
per.setMoney(-5)

# per._Person__money = 1
print(per.getMoney())
#不能直接访问per.__money是因为Python解释器把__money变成了_Person__money

#__XXX__  属于特殊变量