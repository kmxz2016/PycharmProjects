import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
# win.geometry("400x400+200+100")
#EXTENDED 可以使listbox支shift和Ctrl
lb = tkinter.Listbox(win,selectmode=tkinter.EXTENDED)

for item in["good","nice","handsome","cool","very good","奋斗","good","nice","handsome","cool","very good","奋斗"]:
    lb.insert(tkinter.END,item)
#创建滚动条
scroll = tkinter.Scrollbar(win)
#放到窗体哪一侧, fill填充y轴
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
lb.configure(yscrollcommand=scroll.set)
lb.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
scroll['command'] = lb.yview

win.mainloop()