# 题目：海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。
# 第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？
num = int(input("输入猴子的数目:"))


def fn(n):
    if n == num:
        return (4 * x)  # 最后剩的桃子的数目
    else:
        return (fn(n + 1) * 5 / 4 + 1)


x = 1
while 1:
    count = 0
    for i in range(1, num):
        if fn(i) % 4 == 0:
            count = count + 1
    if count == num - 1:
        print("海滩上原来最少有%d个桃子" % int(fn(0)))
        break
    else:
        x = x + 1

print("---------分割线---------")

# if __name__ == '__main__':
#     i = 0  # 猴子数
#     j = 1  # 预设桃子系数
#     x = 0  # 桃子数
#     while i < 5:
#         x = 4 * j   # 假设最后只剩4 * j个桃
#         # 这个循环的目的就是判断每次计算之后的x是不是符合留下来的四倍,符合四倍就一直计算下去,直到满足五个猴子分完
#         for i in range(0, 5):
#             if x % 4 != 0:   # 判断分好后剩下的桃是否刚好是4的倍数,因为分成五份,拿走一份,还剩四份
#                 break
#             else:
#                 i += 1  # 一旦符合四倍就加1,满足一个猴子分桃,直到满足全部的猴子分完桃
#             x = (x / 4) * 5 + 1  # x 这次剩下的桃  x/4表示这次平均分的桃每份的数量,(x / 4) * 5 +1表示上次分桃留下的数量
#         j += 1
#     print(x)
