# 题目：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
a = 10

for i in range(2, 6):  # 后面的人比前面的人大两岁
    a = a + 2
    print("第%d个人%d岁!" % (i, a))


# def age(n, a):
#     if n == 1:
#         return a
#     else:
#         return age(n - 1, a) + 2
#
#
# a = age(5, 10)
# print(a)
