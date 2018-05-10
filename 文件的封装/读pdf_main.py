# -*- coding: UTF-8 -*-
from dealFile import DealFile

d = DealFile()

path = r"/home/km/PycharmProjects/文件的封装/11.pdf"

def func(str):
    print(str + "!")

#回调函数func
d.readPDF(path,func)
