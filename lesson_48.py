# 题目：数字比较。
def compare(a, b):
    if a > b:
        print("%d大于%d" % (a, b))
    elif a == b:
        print("%d等于%d" % (a, b))
    elif b > a:
        print("%d大于%d" % (b, a))
    else:
        print("数字有问题")


if __name__ == '__main__':
    a = int(input("输入第一个数字:"))
    b = int(input("输入第二个数字:"))
    compare(a, b)
