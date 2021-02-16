# 题目：斐波那契数列。
# 后面的数等于前面两个数之和

n = int(input("输出n层斐波那契数列:"))
j = 0
k = 1
for i in range(n):
    print(j, end=" ")
    j, k = k, j + k
