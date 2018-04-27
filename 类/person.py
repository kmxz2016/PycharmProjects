class Person(object):
    def __init__(self,gun):
        self.gun = gun
    def fire(self):
        self.gun.shoot()
    def fillBuiiet(self,count):
        self.gun.clip.bulletCount = count