# 题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
import random

for i in range(7):
    x = random.randint(1, 50)
    print(x, end=' ')
    print("*" * x)
