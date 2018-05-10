import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")

#绑定变量
lbv = tkinter.StringVar()
#与BORWSE相似，但是不支持鼠标按下后选中移动位置
lb = tkinter.Listbox(win,selectmode=tkinter.SINGLE,listvariable=lbv)
lb.pack()
for item in["good","nice","handsome"]:
    lb.insert(tkinter.END,item)
#在开始添加
lb.insert(tkinter.ACTIVE,"cool")
#将列表当成一个元素添加
lb.insert(tkinter.END,["very good","奋斗"])
#打印当前列表中的选项
print(lbv.get())

# lbv.set(("1","2","3","8","6"))
#绑定事件
def myPrint(event):
    print(lb.get(lb.curselection()))
lb.bind('<Double-Button-1>',myPrint)
win.mainloop()