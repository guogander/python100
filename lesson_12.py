# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
from math import ceil
# 设置个标签,要学会这个开关的思想
loop = 1
for i in range(101, 201):
    for j in range(2, int(ceil(i))): # ceil 向上取整
        if i % j == 0:
            loop = 0  # 一旦满足条件就置0
            break
    if loop == 1:  # 判断上次循环是否有满足条件的loop,loop = 1说明没有满足条件就是素数
        print(i)
    loop = 1  # 在下个循环开始前置1
