# 题目：求0—7所能组成的奇数个数。

for i in range(1, 8):
    sum = 4  # 总共的奇数
    s = 4  # 最后一位数的取值情况,只能取奇数,四种1.3.5.7
    if i == 1:  # 组成一位数
        print(i, sum)
    else:  # 组成多位数
        for j in range(1, i + 1):  # 0-7最多可以组成8位数,除去奇数位j要能取到7
            if j == 1:
                s *= 7  # 第一位数除去0有七种取值
            else:
                s *= 8  # 中间几位数有八种取值
            sum += s
        print(i, sum)

else:
    print('0-7能组成的奇数总共有:', sum)

print('-------------分割线----------------')

if __name__ == '__main__':
    sum = 4
    s = 4
    for j in range(2,9):
        print(sum)
        if j <= 2:
            s *= 7
        else:
            s *= 8
        sum += s
    print('sum = %d' % sum)
print('-------------分割线---------------')

# 递归实现
# def f(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 7
#     else:
#         return f(n - 1) * 8
#
#
# l = []
# # 算出每位数有多少奇数
# for i in range(1, 9):
#     l.append(f(i - 1) * 4)
# print(l)
# # 输出一共有多少个奇数
# print(sum(l))
