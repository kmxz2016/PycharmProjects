from person import Person

class Worker(Person):
    def __init__(self,name,age,money):
        #调用父类中的__init__
        super(Worker,self).__init__(name,age,money)