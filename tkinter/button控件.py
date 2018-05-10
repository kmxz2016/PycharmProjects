import tkinter

def func():
    print("km is a handsome man")

win = tkinter.Tk()
win.title("kmxz")

win.geometry("400x400+200+500")

button1 = tkinter.Button(win,text="按钮",command=func,
                        width = 10,
                        height = 5)
button1.pack()

button2 = tkinter.Button(win,text="按钮",command=lambda:print("km is a handsome man"),
                        width = 10,
                        height = 5)
button2.pack()

button3 = tkinter.Button(win,text="退出",command=win.quit)
button3.pack()

win.mainloop()