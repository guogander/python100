# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
import time
t1 = time.time()
for i in range(1, 10000):
    sum = 0
    for j in range(1, i):
        if i % j == 0:  # 找因子
            sum += j   # 找到一个就加起来
    if sum == i:
        print(i)
t2 = time.time()
print(t2-t1)