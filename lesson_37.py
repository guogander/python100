# 题目：对10个数进行排序。
l = []
for i in range(10):
    a = int(input("输入十个数字"))
    l.append(a)
l1 = sorted(l)  # 不改变原序列
l.sort()  # 改变原序列

print(l)
print(l1)

# 自己写算法