import tkinter
from tkinter import ttk

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")

cv = tkinter.StringVar()
com = ttk.Combobox(win,textvariable=cv)
com.pack()
#设置下拉项
com["value"] = ("山西","黑龙江","吉林","辽宁")
#设置默认值
com.current(0)
#绑定事件
def func(event):
    print(com.get())
    print(cv.get())
    print("我在这里")
com.bind("<<ComboboxSelected>>",func)
win.mainloop()