from  person import Person
from student import Student
from worker import Worker

per = Person("tony",1,1)

stu = Student("kevin",28,90,100)
print (stu.name,stu.age)
stu.run()
print(stu.stuId)
# stu.setMoney(76)

print(stu.getMoney())
# print(stu.__Money()) s私有属性
# stu.stuFunc()
print(per.getMoney()) #通过继承过来的共有方法访问私有属性

wor = Worker("Wanghao",26,800)
print (wor.name,wor.age)
wor.eat("apple")