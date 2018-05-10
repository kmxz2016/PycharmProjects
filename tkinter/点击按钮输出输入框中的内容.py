import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")

def showInfo():
    print(entry.get())

entry = tkinter.Entry(win)
entry.pack()

button = tkinter.Button(win,text="按钮",command=showInfo)
button.pack()


win.mainloop()