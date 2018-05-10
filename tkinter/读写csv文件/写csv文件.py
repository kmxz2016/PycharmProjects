import csv

def writeCsv(path,data):
    with open(path,"w") as f:
        writer = csv.writer(f)
        for rowData in data:
            print("rowData=",rowData)
            writer.writerow(rowData)



path = r"/home/km/PycharmProjects/tkinter/读写csv文件/2.csv"
writeCsv(path,[[1,2,3],[1,2,3],[1,2,3]])