"""
人
类名：Person
属性：gun
行为：fire

枪
类名：Gun
属性：clip
行为：shooting

弹夹
类名：Clip
属性：bulletCount
行为：


"""

from  person import  Person
from  gun import Gun
from clip import Clip

clip = Clip(5)
gun = Gun(clip)
per = Person(gun)

per.fire()
per.fire()
per.fire()
per.fire()
per.fire()

per.fillBuiiet(8)
per.fire()
per.fire()