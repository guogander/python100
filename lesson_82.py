# 题目：八进制转换为十进制
# a = int(input("输入一个十进制数:"))  # 十进制
# b = oct(a)  # 八进制
# print("十进制%d对应的八进制数是%d"%(a, b))

c = input("输入一个八进制数:")  # 接收的是字符串类型
l1 = []
d = 0  # 十进制
for i in c:
    l1.insert(0, i)  # 将输入的数字当做字符串的每一位反向插入到列表中
# print(l1)
for j in range(len(c)):
    d = d + int(l1[j]) * 8 ** j  # 按权展开 相加
print("%s的十进制是%d" % (c, d))
