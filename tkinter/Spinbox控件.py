import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")


"""
数值范围控件

"""
def update():
    print(v.get())
#绑定变量
v = tkinter.StringVar()
#command只要值改变就会执行对应的方法
sp = tkinter.Spinbox(win,from_=0,to=100,increment=5,textvariable=v,command=update)
#values不要和from_=0,to=100,increment=5同时使用
# sp = tkinter.Spinbox(win,values=(0,2,4,6,8))
sp.pack()
v.set(30)
print(v.get())
win.mainloop()