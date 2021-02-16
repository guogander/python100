# 题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

# 偶数求和
def sum_ou(n):
    s = 0.0
    for i in range(1, n // 2 + 1):
        s = s + 1 / (2 * i)
    print("输入的n为偶数,1/2+1/4+...+1/%d = " % n, s)


# 奇数求和
def sum_ji(n):
    s = 0.0
    for i in range(1, n // 2 + 1):
        s = s + 1 / (2 * i - 1)
    print("输入的n为奇数,1/1+1/3+...+1/%d = " % n, s)


if __name__ == '__main__':
    n = int(input("输入一个正整数:"))
    if n % 2 == 0:
        sum_ou(n)
    else:
        sum_ji(n)
