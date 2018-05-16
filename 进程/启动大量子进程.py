from multiprocessing import Pool
import os,time,random

def run(name):
    print("子进程%d启动--%s"%(name,os.getpid()))
    start = time.time()
    time.sleep(random.choice([1,2,3]))
    end = time.time()
    print("子进程%d结束--%s--耗时%.2f"%(name,os.getpid(),end-start))

if __name__ == "__main__":
    print("父进程开始")
    #创建多个进程
    #进程池
    #表示可以同时执行的
    #Pool默认是cpu核心数
    pp = Pool()
    for i in range(4):
        #创建进程，放入进程池，统一管理
        pp.apply_async(run,args=(i,))
    #在调用join之前必须先调用close,调用close之后就不能再继续添加新的进程了
    pp.close()
    #进程池调用了join，会等待进程池中所有的子进程结束完毕再去执行父进程
    pp.join()
    print("父进程结束")
