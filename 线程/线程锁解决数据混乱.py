import threading
#锁对象
lock = threading.Lock()
num = 100
def run(n):
    global num
    for i in range(1000000):
        #锁,确保了这段代码只能由一个线程从头到尾完整执行
        #阻止了多线程的并发执行，包含锁的某段代码实际上只能以单线程模式执行，所以大大降低了效率
        """
        lock.acquire()
        try:
            num = num + n
            num = num - n
        finally:
            #修改完释放锁
            lock.release()
        """
        with lock:
            num = num + n
            num = num - n
if __name__ == "__main__":
    t1 = threading.Thread(target=run,args=(6,))
    t2 = threading.Thread(target=run,args=(9,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("num = ",num)