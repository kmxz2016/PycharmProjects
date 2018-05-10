import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")
#<Button-1>鼠标左键
#<Button-2>鼠标中键
#<Button-3>鼠标右键
#<Double-Button-1>鼠标左键双击
#<Double-Button-2>鼠标中键双击
#<Double-Button-3>鼠标右键双击

#<Triple-Button-1>鼠标左键三击
#<Triple-Button-2>鼠标中键三击
#<Triple-Button-3>鼠标右键三击
def func(event):
    print(event.x,event.y)
button1 = tkinter.Button(win,text="leftmouse button")
# button1 = tkinter.Label(win,text="leftmouse button")
#bind给控件绑定事件
button1.bind("<Double-Button-1>",func)
button1.pack()


win.mainloop()