data = [["姓名","爱好","年龄"],["km","无","27"],["韩磊","money","28"]]
def func2(v):
    v = str(v)
    if v == "无":
        return False
    return True
for line in data:
    m = filter(func2,line)
    print (list(m))