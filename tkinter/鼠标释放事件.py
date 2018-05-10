import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")
# <ButtonRelease-1>释放鼠标左键
# <ButtonRelease-2>释放鼠标中键
# <ButtonRelease-3>释放鼠标右键

label1=tkinter.Label(win,text="hard",bg="blue")
label1.pack()

def func(event):
    print(event.x,event.y)
label1.bind("<ButtonRelease-1>",func)


win.mainloop()