"""
判断字符串是否是手机号码
"""
def checkPhone(str):
    if len(str) !=11:
        return False
    elif str[0] !="1":
        return False
    elif str[1:3] != "36" and str[1:3] != "31" :
        return False
    for i in str:
        if i < "0" or i > "9":
            return False
    """
    for i in range(3,11):
        if str[i] < "0" or str[i] > "9":
            return False
    """
    return True

print(checkPhone("13676480081"))
print(checkPhone("13476480081"))
print(checkPhone("13676s0081"))
print(checkPhone("13676b80081"))
print(checkPhone("13176480081"))
