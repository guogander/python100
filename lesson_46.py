# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。
while 1:
    n = int(input("输入一个数字:"))
    s = n * n
    print("%d的平方是%d:" % (n, s))
    if s < 50:
        break
