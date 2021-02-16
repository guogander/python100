# 题目：学习使用auto定义变量的用法。
num = 2  # 全局变量


def autofunc():
    # num = 1  # 局部变量
    global num
    num = 1
    a = 1
    a += num
    print('internal block num = %d' % num)
    # num += 1  # 这个只影响函数内的局部变量,每次调用这个函数都会被置为1,此行无实际意义


if __name__ == '__main__':
    print(num)
    for i in range(3):
        print('The num = %d' % num)
        num += 1  # 这个改变的是全局变量
        autofunc()

# num = 2
# def autofunc():
#     a = 1
#     a += num
#     print('internal block num = %d' % num)
#
# for i in range(3):
#     print('The num = %d' % num)
#     num += 1
#     autofunc()
