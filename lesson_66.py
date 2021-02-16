# 题目：输入3个数a,b,c，按大小顺序输出。
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
l = [a, b, c]
l.sort(reverse=True)  # 大到小排序
for i in range(3):
    print(l[i])
