# 题目：求1+2!+3!+...+20!的和。
# s = 0  # 和
# for i in range(1, 21):
#     t = 1
#     for j in range(1, i + 1):  # 求每个数的阶乘
#         t = t * j
#         # if j == i:
#         #     print("%d! " % i, end="")
#     s += t
# print("1!+2!+3!+...+20!=", s)

# 递归函数实现
def jieCheng(n):
    s = 0
    t = 1
    for i in range(1, n + 1):
        t = t * i
    s += t
    if n == 1:
        return s
    else:
        return s + jieCheng(n - 1)


s = jieCheng(20)
print(s)
