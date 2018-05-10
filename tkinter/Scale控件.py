import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")


"""
供用户通过拖拽改变变量的值，可以水平，也可以竖直
tkinter.HORIZONTAL 竖直
tkinter.VERTICAL  水平

length水平时是宽度，竖直时是高度
tickinterval 所选值将是倍数
"""

scale = tkinter.Scale(win,from_=0, to=100,orient=tkinter.HORIZONTAL,tickinterval=10,length=200)
scale.pack()
#设置值
scale.set(20)
def showNum():
    print(scale.get())
tkinter.Button(win,text="按钮",command=showNum).pack()
# print(scale.get())



win.mainloop()