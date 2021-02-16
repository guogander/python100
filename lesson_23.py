# 题目：打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

# # 上部分
for i in range(1, 5):
    print(' ' * (4 - i), end="")  # 打印每行前面的空格
    for j in range(1, 2 * i):
        print("*", end='')  # 循环2*i-1次,打印这么多*
    print()
# 下部分
for i in range(1, 4):
    print(' '*i, end='')   # 打印每行前面的空格
    for j in range(1, 8 - 2 * i):   # 计算*和行数的关系
        print('*', end='')
    print()






# for i in range(1, 5):
#     print(' ' * (4 - i), end="")
#     for j in range(1, 2 * i):
#         print('*', end="")
#     print()
