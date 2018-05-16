from multiprocessing import Process
from time import sleep
import os

def run(str):
    while True:
        #os.getpgid()获取当前进程ID号
        #os.getppid()获取当前进程父进程ID号
        print("狂迷小子%s加油--%s--%s"%(str,os.getpid(),os.getppid()))
        sleep(1.2)

if __name__ == "__main__":
    print("主进程启动-%s" %(os.getpid()))
    p = Process(target=run,args=("妈妈爱你,",))
    p.start()
    while True:
        print("小子最棒！！！")
        sleep(1)
