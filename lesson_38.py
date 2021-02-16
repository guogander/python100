# 题目：求一个3*3矩阵主对角线元素之和。
"""
1 2 3
4 10 6
7 8 9
"""
a = [[1, 2, 3], [4, 10, 6], [7, 8, 9]]
s = 0
# s = a[0][0] + a[1][1] + a[2][2]

# 主对角线
for i in range(3):
    for j in range(3):
        if i == j:
            s += a[i][i]
print(s)

# 副对角线
s1 = 0
for i in range(3):
    for j in range(2, -1, -1):
        if i + j == 2:
            s1 += a[i][j]
print(s1)
