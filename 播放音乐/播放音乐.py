# -*- coding: UTF-8 -*-
import time
import pygame

#sudo apt-get install python-pygame

filePath = "/home/km/PycharmProjects/播放音乐/张碧晨-红玫瑰.mp3"
#初始化
pygame.mixer.init()

#加音乐
track = pygame.mixer.music.load(filePath)

#播放
pygame.mixer.music.play()
#暂停
time.sleep(10)
pygame.mixer.music.pause()
#停止
pygame.mixer.music.stop()