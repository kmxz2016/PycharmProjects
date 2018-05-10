import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")

label1=tkinter.Label(win,text="hard")
label1.pack()

def func(event):
    print(event.x,event.y)
label1.bind("<B1-Motion>",func)


win.mainloop()