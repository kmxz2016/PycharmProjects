"""
一个进程的内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”叫做线程

线程通常叫做轻型的进程，线程是共享内存空间的并发执行的多任务，每一个线程都共享一个进程的资源

线程是最小的执行单元，而进程至少由一个线程组成，如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间

"""
import threading,time

a = 10
def run(num):
    print("子线程（%s）启动" % (threading.current_thread().name))
    time.sleep(2)
    print("打印",num)
    time.sleep(2)
    print(a)
    print("子线程（%s）启动" % (threading.current_thread().name))
if __name__ == "__main__":
    #任何进程默认就会启动一个线程，称为主线程，主线程可以启动新的子线程
    #current_thread()返回当前线程的实例
    print("主线程（%s）启动" % (threading.current_thread().name))
    #创建子线程
    t = threading.Thread(target=run,name="runThread",args=(1,))
    t.start()
    print("主线程（%s）结束" % (threading.current_thread().name))