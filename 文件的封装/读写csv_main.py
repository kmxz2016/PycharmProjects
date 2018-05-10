# -*- coding: UTF-8 -*-
from dealFile import DealFile

d = DealFile()

toPath = r"/home/km/PycharmProjects/文件的封装/toTracePath.csv"
for i in range(2,5):
    # path = r"/home/km/PycharmProjects/文件的封装/TracePath.csv" + str(i) + ".csv"
    path = r"/home/km/PycharmProjects/文件的封装/TracePath.csv"
    listInfo = d.readCsv(path)

    d.writeCsv(toPath,listInfo)

allInfo = d.readCsv(toPath)

