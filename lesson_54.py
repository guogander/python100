# 题目：取一个整数a从右端开始的4〜7位。
a = int(input("输入数字:"))
b = a >> 4
c = 0x0f  # 00001111
d = b & c
print("0x%x,%o" % (a, d))
