import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")

"""
框架控件，在屏幕上可以显示一个矩形区域，多作为容器控件

"""
frm = tkinter.Frame(win)
frm.pack()

#left
# frm_l = tkinter.Frame(frm)
frm_l = tkinter.Frame(win)
tkinter.Label(frm_l,text="左上",bg="pink").pack(side=tkinter.TOP)
tkinter.Label(frm_l,text="左下",bg="blue").pack(side=tkinter.TOP)
frm_l.pack(side=tkinter.LEFT)

#right
# frm_r = tkinter.Frame(frm)
frm_r = tkinter.Frame(win)
tkinter.Label(frm_r,text="右上",bg="red").pack(side=tkinter.TOP)
tkinter.Label(frm_r,text="右下",bg="yellow").pack(side=tkinter.TOP)
frm_r.pack(side=tkinter.RIGHT)

win.mainloop()