from animal import Animal

class Cat(Animal):
    def __init__(self,name):
        super(Cat, self).__init__(name)
        # self.name = name
    # def eat(self):
    #     print(self.name +"吃")