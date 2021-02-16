# 题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
n = int(input("输入一个奇数:"))

num = 9
i = 1
while not (num / n % 1 == 0):  # num/n 为结果,如果结果对1取余数为0 则为整数
    num = 10 * num + 9  # 产生9的循环
    i += 1
print("%d个9才能整除%d" % (i, n))

print("-----------分割线--------------")


num = 9
i = 1
while not num % n == 0:
    num = 10 * num + 9
    i += 1
print("%d个9才能整除%d" % (i, n))
