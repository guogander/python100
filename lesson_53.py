# 题目：学习使用按位异或 ^ 。
# 按位异或运算符：当两对应的二进位相异时，结果为1

# 0x77 = 01110111
#    3 = 00000011
x = 0x77 ^ 3  # 01110100 = 0x74 = 116
print(x)  # 116