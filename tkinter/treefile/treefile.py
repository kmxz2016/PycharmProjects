import tkinter
import os
from treeWindows import TreeWindows
from infoWindows import InfoWindows

win = tkinter.Tk()
win.title("km")
win.geometry("900x400+200+50")

# path = "/home/km/baxter_ws/src"
path = r"/home/km/baxter_ws/src"
infoWin = InfoWindows(win)
treeWin = TreeWindows(win,path,infoWin)




win.mainloop()