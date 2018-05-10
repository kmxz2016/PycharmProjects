import csv
def readCsv(path):
    with open(path,"r") as f:
        allFileInfo = csv.reader(f)
        print(allFileInfo)
        for row in allFileInfo:
            print(row)

path = r"/home/km/PycharmProjects/tkinter/读写csv文件/TracePath.csv"
info = readCsv(path)
