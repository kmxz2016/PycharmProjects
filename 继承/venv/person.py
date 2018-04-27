class Person(object):
    def __init__(self,name,age,money):
        self.name =name
        self.age = age
        self.__money =money

    def setMoney(self,money):
        #数据过滤
        if money < 0:
            money = 0
        self.__money = money

    def getMoney(self):
        return self.__money

    def run(self):
        print ("run")
    def eat(self,food):
        print ("eat",food)