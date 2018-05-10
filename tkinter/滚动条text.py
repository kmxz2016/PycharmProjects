import tkinter

#创建主窗口
win = tkinter.Tk()
win.title("kmxz")
#设置大小和位置
# win.geometry("400x400+200+100")


"""
文本控件，用于显示多行文本

"""
#创建滚动条
scroll = tkinter.Scrollbar()
#放到窗体哪一侧, fill填充y轴
scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)

text = tkinter.Text(win,width=30,height=4)
text.pack(side=tkinter.LEFT,fill=tkinter.Y)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

str = '''Chief Justice Roberts, President Carter, President Clinton, President Bush, President Obama, fellow Americans and people of the world, thank you.
We, the citizens of America, are now joined in a great national effort to rebuild our country and restore its promise for all of our people. Together we will determine the course of America and the world for many, many years to come.
We will face challenges. We will confront hardships. But we will get the job done. Every four years, we gather on these steps to carry out the orderly and peaceful transfer of power.
And we are grateful to President Obama and First Lady Michelle Obama for their gracious aid throughout this transition. They have been magnificent. Thank you.'''
text.insert(tkinter.INSERT,str)


win.mainloop()