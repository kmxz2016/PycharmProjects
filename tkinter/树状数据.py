import tkinter
from tkinter import ttk
#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
win.geometry("400x400+200+100")

tree = ttk.Treeview(win)
tree.pack()
#添加一级树枝
treeF1 = tree.insert("",0,"中国",text="中国C",values=("F1"))
treeF2 = tree.insert("",1,"美国",text="美国USA",values=("F2"))
treeF3 = tree.insert("",2,"英国",text="英国UK",values=("F3"))
#添加二级树枝
treeF1_1 = tree.insert(treeF1,0,"黑龙江",text="中国黑龙江",values=("F1_1"))
treeF1_2 = tree.insert(treeF1,1,"山西",text="中国山西",values=("F1_2"))
treeF1_3 = tree.insert(treeF1,2,"温州",text="中国温州",values=("F1_3"))

treeF2_1 = tree.insert(treeF2,0,"德克萨斯",text="美国德克萨斯",values=("F2_1"))
treeF2_2 = tree.insert(treeF2,1,"旧金山",text="美国旧金山",values=("F2_2"))
treeF2_3 = tree.insert(treeF2,2,"华尔街",text="美国华尔街",values=("F2_3"))

#添加三级树枝
treeF1_1_1 = tree.insert(treeF1_1,0,"哈尔滨",text="黑龙江哈尔滨",values=("F1_1_1"))
win.mainloop()