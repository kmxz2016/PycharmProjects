class Gun(object):
    def __init__(self,clip):
        self.clip = clip
    def shoot(self):
        if self.clip.bulletCount == 0:
            print("没有子弹")
        else:
            self.clip.bulletCount -= 1
            print("剩余子弹:%d 发" %(self.clip.bulletCount))