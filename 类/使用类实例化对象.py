class Person(object):
    name = ""
    age = 0
    height = 0
    weight= 0
    def run (self):
        print("run")
    def eat (self,food):
        print("eat", food)
    def openDoor(self):
        print("打开冰箱")
    def fillEle(self):
        print("我已经把大象装好了")
    def closeDoor(self):
        print("关闭")

per1 = Person()
print(per1)
print(type(per1))
print(id(per1))

per2 = Person()
print(per2)
print(type(per2))
print(id(per2))

"""
访问属性
格式：对象名.属性名
赋值：对象名.属性名 = 新值
"""
per = Person()
per.name ="km"
per.age = 28
per.height = 173
per.weight = 75
print(per.name,per.age,per.height,per.weight)

"""
访问方法
格式：对象名.方法名(参数列表)

"""
per.openDoor()
per.fillEle()
per.closeDoor()

per.eat("apple")