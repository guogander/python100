# 题目：学习使用按位与 & 。
# 按位运算符是把数字看作二进制来进行计算的。按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
# 0x77 = 01110111
#    3 = 00000011
x = 0x77 & 3  # 00000011
print(x)