"""
self代表类的实例，非类
哪个对象调用方法，那该方法中的self就代表哪个对象
self.__class__  代表类型

"""
class Person(object):
    def run (self):
        print("run")
        print(self.__class__)
        p = self.__class__("tt",30,40,10)
        print(p)
    def eat (self,food):
        print("eat", food)
    def say(self):
        print("Hello! My name is %s,I am %d years old"
              %(self.name,self.age))
    #self不是关键字,可以用标识符代替，但大家都用self
    def play(a):
        print("play",a.name)
    def __init__(self,name,age,height,weight):
        self.name =name
        self.age = age
        self.height = height
        self.weight = weight


per = Person("hamei",20,173,74)
per.say()
per.play()

per1 = Person("wanghao",26,183,78)
per1.say()
per1.run()