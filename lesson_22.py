# 题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
import time

# m = ['x', 'y', 'z']
# for a in m:
#     for b in m:
#         for c in m:
#             if (a != 'x') and (c != 'x') and (c != 'z') and (a != b) and (a != c) and (c != b):  # 同队不能一样,然后加上条件
#                 print("a--%s,b--%s,c--%s" % (a, b, c))


m = ['x', 'y', 'z']
for a in m:
    if a != 'x':  # 条件在这里会少执行几次
        for c in m:
            if (c != 'x') and (c != 'z'):
                for b in m:
                    if (a != b) and (a != c) and (c != b):  # 同队不能一样
                        print("a--%s,b--%s,c--%s" % (a, b, c))

