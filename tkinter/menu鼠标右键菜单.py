import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")

#菜单条
menubar = tkinter.Menu(win)

#创建菜单选项
menu1 = tkinter.Menu(menubar,tearoff=False)
for itme in ["Python","C","C++","OC","Swift","C#","shell","Java","JS","PHP","汇编","NodeJs","退出"]:
    menu1.add_command(label=itme)
#向菜单选项上添加菜单
menubar.add_cascade(label="语言",menu=menu1)
def showMenu(event):
    menubar.post(event.x_root,event.y_root)
win.bind("<Button-3>",showMenu)
win.mainloop()