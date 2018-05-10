
class Person(object):
    def __init__(self,name,age):
        #属性直接对外暴露
        self.__age = age
        self.__name = name

    # def getAge(self):
    #     return self.__age
    # def setAge(self,age):
    #     if age < 0:
    #         age = 0
    #     self.__age = age

    #方法名为受限制的变量去掉双下划线
    @property
    def age(self):
        return self.__age
    #去掉下划线
    @age.setter
    def age(self,age):
        if age < 0:
            age = 0
        self.__age = age
    #property让你可以对受限制访问的属性使用点语法
    @property
    def name(self):
        return self.__name

    # 去掉下划线
    @name.setter
    def name(self, name):
        self.__name = name


per = Person("Kevin",18)



#使用限制访问需要自己写set 和get方法
# per.setAge(18)
# print(per.getAge())

# per.age = 100
# per.name = "Kevin"
print(per.age)
print(per.name)