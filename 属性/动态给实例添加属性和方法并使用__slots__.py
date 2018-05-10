from types import MethodType
#创建一个空类
class Person(object):
    pass
    #限制动态添加的属性
    # __slots__ = ("name","age")


per = Person()
#动态添加属性，这体现了动态与语言的特点（灵活）
per.name = "Kevin"
print(per.name)
#动态添加方法
def say(self):
    print("my name is",self.name)
# per.speak = say()
# per.speak()
per.speak = MethodType(say,per)
per.speak()

#思考：如果我们想要限制实例的属性怎么办？