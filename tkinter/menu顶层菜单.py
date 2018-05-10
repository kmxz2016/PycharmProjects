import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")

#菜单条
menubar = tkinter.Menu(win)
win.config(menu=menubar)

def func():
    print("km is a good boy")
#创建菜单选项
menu1 = tkinter.Menu(menubar,tearoff=False)
for itme in ["Python","C","C++","OC","Swift","C#","shell","Java","JS","PHP","汇编","NodeJs","退出"]:
    if itme == "退出":
        #添加分割线
        menu1.add_separator()
        menu1.add_command(label=itme,command=win.quit)
    else:
        menu1.add_command(label=itme,command=func)
#向菜单选项上添加菜单
menubar.add_cascade(label="语言",menu=menu1)

menu2 = tkinter.Menu(menubar,tearoff=False)
menu2.add_command(label="红色")
menu2.add_command(label="蓝色")
menubar.add_cascade(label="颜色",menu=menu2)

win.mainloop()