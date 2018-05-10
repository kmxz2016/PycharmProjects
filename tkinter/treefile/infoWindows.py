import tkinter
from tkinter import ttk
import os


class InfoWindows(tkinter.Frame):
    def __init__(self,master):
        frame = tkinter.Frame(master)
        frame.grid(row=0,column=1)



        self.ev = tkinter.Variable()
        self.entry = tkinter.Entry(frame,textvariable=self.ev)
        self.entry.pack()

        self.txt = tkinter.Text(frame)
        self.txt.pack()
