from cat import Cat
from mouse import Mouse
from person import Person


"""
多态：一种事物的多种形态
最终目标：人可以喂任何一种动物


"""
tom = Cat("tom")
jeff = Mouse("jeff")


per = Person()
# per.feedCat(tom)
# per.feedMouse(tom)
per.feedAnimal(tom)




tom.eat()
jeff.eat()