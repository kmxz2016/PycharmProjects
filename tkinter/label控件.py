import tkinter

win = tkinter.Tk()
win.title("kmxz")
win.geometry("400x400+200+100")

"""
Label:标签控件，可以显示文本
"""
#win:父窗体
#bg 背景色
#wraplength 指定文本多宽，然后换行
#anchor "n、e、s、w、
label = tkinter.Label(win,
                      text="km is a handsome man",
                      bg="blue",
                      fg="red",
                      width=10,
                      height=3,
                      wraplength=100,
                      font=("黑体",20),
                      justify="left",
                      anchor="n")
label.pack()




win.mainloop()