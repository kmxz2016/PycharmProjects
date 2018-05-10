import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")

label1=tkinter.Label(win,text="hard",bg="blue")
label2=tkinter.Label(win,text="good",bg="red")
label3=tkinter.Label(win,text="cool",bg="pink")

label1=tkinter.Label(win,text="hard",bg="blue")
label2=tkinter.Label(win,text="good",bg="red")
label3=tkinter.Label(win,text="cool",bg="pink")
label4=tkinter.Label(win,text="handsome",bg="yellow")
#表格布局
label1.grid(row=0,column=0)
label2.grid(row=0,column=1)
label3.grid(row=1,column=0)
label4.grid(row=1,column=1)


win.mainloop()