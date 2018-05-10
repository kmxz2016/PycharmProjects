import csv
def readCsv(path):
    infoList = []
    with open(path,"r") as f:
        allFileInfo = csv.reader(f)
        print(allFileInfo)
        for row in allFileInfo:
            infoList.append(row)
    return infoList

path = r"/home/km/PycharmProjects/tkinter/读写csv文件/TracePath.csv"
info = readCsv(path)
