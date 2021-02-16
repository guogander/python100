# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

def rabbit(num):
    f1 = 1
    # 第一个月为1
    f2 = 1
    # 第二个月为1
    if num == 1 or num == 2:
        return 1
    else:
        for i in range(num - 1):
            f1, f2 = f2, f1 + f2
    return f1


print(rabbit(42))

# 此题解法与斐波拉切数列一致
