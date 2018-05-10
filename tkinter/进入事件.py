import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")

# <Enter>鼠标光标进入控件时触发
# <Leave>鼠标光标离开控件时触发
label1=tkinter.Label(win,text="hard",bg="blue")
label1.pack()

def func(event):
    print(event.x,event.y)
label1.bind("<Enter>",func)


win.mainloop()