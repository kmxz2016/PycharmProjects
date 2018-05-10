import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")
#MULTIPLE 多选
lb = tkinter.Listbox(win,selectmode=tkinter.MULTIPLE)
lb.pack()
for item in["good","nice","handsome","cool","very good","奋斗","good","nice","handsome","cool","very good","奋斗"]:
    lb.insert(tkinter.END,item)

win.mainloop()