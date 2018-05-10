import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")


#绑定变量
e = tkinter.Variable()
#输入控件，用于显示简单的文本内容
entry = tkinter.Entry(win,textvariable=e)
entry.pack()

#e代表输入框这个对象
#设置值
e.set("我是狂迷小子")
print(e.get())
print(entry.get())



win.mainloop()