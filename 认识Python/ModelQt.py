# coding=utf-8
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushbutton,QProgressBar
from PyQt5.QtCore import QBasicTimer

    #构建窗口类
class Example(QWidget):
    #self是类实例对象的本身
    def __init__(self):
        #解决多重继承问题
        super().__init__()
        #调用UI
        self.initUI()
        #点击按钮
        self.btn.clicked.connect(self.doAction)  #信号和槽
    #绘制UI界面
    def initUI(self):
        #构建进度条
        self.pbar=QProgressBar(self)
        #
        self.pbar.setGeometry(30,50,200,25)
        #构建按钮
        self.btn=QPushbutton('运行',self)
        #按钮的移动位置
        self.btn.move(50,90)
        #激活进度条
        self.timer=QBasicTimer()
        #进度条的起始值
        self.step=0
        self.setGeometry(300,300,280,175)
        self.setWindowTitle('km的进度条')
        self.show()
    def timerEvent(self,*args,**kwargs):
        if self.step >=100:
            self.timer.stop()
            self.btn.setText("完成")
            return
        self.step=self.step+1
        #重置进度条
        self.pbar.setValue(self.step)
    def doAction(self):
        #判断是否已经激活进度条
        if self.timer.isActive():
            #停止
            self.timer.stop()
            self.btn,setText("开始")
        else:
            #启动
            self.timer.start(100,self)
            self.btn,setText("停止")

# def km(*args,**kwargs):
#     print("*args====",args)
#     print("**kwargs====",kwargs)


if  __name__=='__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
    # km(km(1,2,3))