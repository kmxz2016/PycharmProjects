import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")

label1=tkinter.Label(win,text="hard",bg="blue")
#设置焦点
label1.focus_set()
label1.pack()
# <Key>响应所有事件

def func(event):
    print("event.char=",event.char)
    print("event.keycode=", event.keycode)
label1.bind("<d>",func)

win.mainloop()