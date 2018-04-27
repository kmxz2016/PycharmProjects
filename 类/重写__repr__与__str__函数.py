"""
重写：将函数重新定义写一遍

__str__(self): 在调用print打印对象时自动调用，他是给用户用的，是一个描述对象的方法

__repr__(self):是给机器用的，在Python解释器里直接敲对象名，在回车后调用的方法

注意：在没有__str__(self):时，且有__str__(self): = __repr__(self):
"""
class Person(object):
    def __init__(self,name,age,height,weight):
        self.name =name
        self.age = age
        self.height = height
        self.weight = weight
    # def __repr__(self):
    #     print("这里是repr")

    def __str__(self):
        return"%s-%d-%d-%d" %(self.name,self.age,self.height,self.weight)
per = Person("hanmeimei",20,173,74)
# print(per.name,per.age,per.height,per.weight)

#当一个对象的属性值很多，并且都需要打印时，重写了__str__方法后，简化了代码
print(per)

