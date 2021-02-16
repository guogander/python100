# 题目：写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。

# 自定义函数
def len_str(str):
    j = 0
    if s != "":
        for i in str:
            j += 1
        print("自定义函数计算字符数:", j)

    else:
        print("自定义函数计算字符数:", j)


if __name__ == '__main__':
    s = input("输入一串字符:")
    len_str(s)
    print("len()方法计算字符数:", len(s))
