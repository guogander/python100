# 题目：将一个列表的数据复制到另一个列表中。程序分析：使用列表[:]。
list1 = [1, 2, 3]
list2 = list1
list3 = list1[:] # 切片
print(list2,list3)
