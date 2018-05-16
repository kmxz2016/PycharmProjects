from multiprocessing import Process
from time import sleep

num = 100
def run():
    print("子进程启动")
    global num
    num +=1
    print(num)
    print("子进程结束")
if __name__ == "__main__":
    print("父进程开始")
    p = Process(target=run)
    p.start()
    p.join()
    #子进程中修改全局变量对父进程中无影响
    #在创建子进程时对全局变量做了备份，父进程中和子进程中的num完全不同
    print("父进程结束--%d"%num)