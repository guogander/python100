# 题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。
import time
import random

print('猜数字游戏(1-100)!')
n = int(input("输入你猜的数字:"))
start = time.perf_counter()
randNum = random.randint(1, 100)

while 1:
    if n == randNum:
        end = time.perf_counter()
        print("猜对了,你上一轮猜数字花了%.2f秒" % (end-start))
        t = input("还要继续玩吗(N退出)?按任意键继续!")
        if t == 'N':  # 退出
            break
        else:  # 继续
            randNum = random.randint(1, 100)
    elif n < randNum:
        print("输入的数小了点!")
    elif n > randNum:
        print("输入的数大了点!")
    else:
        print("请正确输入!")
    n = int(input("继续输入你猜的数字:"))