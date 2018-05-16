#升序
list1 = [4,6,7,8,9,5,4]
list2 = sorted(list1)
print(list2)

#绝对值排序
list3 = [4,-6,7,8,-9,-5,4]
list4 = sorted(list3,key=abs)
print(list4)

#降序
list5 = [4,6,7,8,9,5,4]
list6 = sorted(list5,reverse=True)
print(list6)

#降序
list7 = ["eewew4","fffefe6","7","ffgfg8","fbbb9","fgfggfgbbb5"]
list8 = sorted(list7,key=len)
print(list8)