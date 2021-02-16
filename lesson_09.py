# 题目：暂停一秒输出。
import time

for i in range(1,10):
    for j in range(1,10):
        if j <= i:
            print("%d * %d = %d"%(j, i, i * j), end=' ')
    time.sleep(1) # 打印一行暂停一秒
    print()