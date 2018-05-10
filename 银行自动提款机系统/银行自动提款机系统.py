"""人
类名：User
属性：姓名、身份证号、电话号、卡
行为：

卡
类名：Card
属性：卡号、密码、余额

银行
类名：bank
属性：用户列表、提款机

提款机
类名：ATM
属性：用户字典
行为：开户、查询、取款、存储、转账、改密、锁定、解锁、补卡、销户

管理员
类名：Admin
属性：
行为：管理员界面、管理员登录、系统功能界面
"""
from admin import Admin
from atm import Atm
import pickle
import time
import os
def main():

    #管理员对象
    admin = Admin()
    #管理员开机
    admin.printAdminView()
    if admin.adminOption():
        return -1

    # 存储所有用户信息
    allUsers = {}

    #提款机对象

    filepath = os.path.join(os.getcwd(), "allusers.txt")
    f = open(filepath,"rb")
    allUsers = pickle.load(f)
    print("*******")
    print(allUsers)
    atm = Atm(allUsers)


    while True:
        #等待用户操作
        admin.printSysFunctionView()
        option  = input("请您操作：")
        if option == "1":
            atm.createUser()
        elif option == "2":
            atm.searchUserInfo()
        elif option == "3":
            atm.getMoney()
        elif option == "4":
            print("存储")
        elif option == "5":
            print("转账")
        elif option == "6":
            print("改密")
        elif option == "7":
            atm.lockUser()
        elif option == "8":
            atm.unlockUser()
        elif option == "9":
            print("补卡")
        elif option == "10":
            print("销户")
        elif option == "t":
            if not admin.adminOption():
                # 保存信息
                filepath = os.path.join(os.getcwd(), "allusers.txt")
                f = open(filepath,"wb")
                pickle.dump(atm.allUsers,f)
                f.close()
                return -1
            # else:

        time.sleep(2)


if __name__ == "__main__":
    main()