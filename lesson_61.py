# 题目：打印出杨辉三角形（要求打印出10行如下图）。
"""
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1
"""
# a = []
# for i in range(10):
#     for j in range(1, i + 2):
#         a.append(i)
#         print(j, end='')
#     else:
#         print(a)

n = 10


def lst(i, j):
    if i == j or j == 1:  # j == 1判断第一列.i == j判断每一行最后一个数字为1
        return 1
    else:
        return lst(i - 1, j - 1) + lst(i - 1, j)


for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(lst(i, j), end=' ')  # 此处增加断点一步步调试可以看出,每一步都是去调用上一步的结果进来运算
    else:
        print()
