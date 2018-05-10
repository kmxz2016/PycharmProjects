from child import Child

def main():
    c = Child(300,100)
    print(c.money,c.faceValue)
    c.play()
    c.visit()
    #父类中的方法名相同，默认调用的是括号中排前面的父类中的方法
    c.work()
if __name__ == "__main__":
    main()