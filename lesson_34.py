# 题目：练习函数调用。
#
# 程序分析：使用函数，输出三次 RUNOOB 字符串。

def runoob():
    print("RUNOOB")


def hello():
    for i in range(3):
        runoob()


hello()
