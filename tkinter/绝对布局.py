import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")

label1=tkinter.Label(win,text="hard",bg="blue")
label2=tkinter.Label(win,text="good",bg="red")
label3=tkinter.Label(win,text="cool",bg="pink")



#绝对布局,窗口的变换对位置没有影响
label1.place(x=10,y=10)
label2.place(x=30,y=30)
label3.place(x=50,y=50)



win.mainloop()