import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")

label1=tkinter.Label(win,text="hard",bg="blue")
label2=tkinter.Label(win,text="good",bg="red")
label3=tkinter.Label(win,text="cool",bg="pink")



#相对布局,窗口的变换对控件有影响
label1.pack(fill=tkinter.Y,side=tkinter.LEFT)
label2.pack(fill=tkinter.X,side=tkinter.TOP)
label3.pack(fill=tkinter.Y,side=tkinter.RIGHT)



win.mainloop()