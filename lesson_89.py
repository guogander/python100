# 题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
msg = input("输入四位整数:")  # 加密前
l1 = []
for i in msg:
    l1.append((int(i) + 5) % 10)  # 将输入的数字字符分开+5对10取余存入列表
# print(l1)
# for j in range(4):
#     l1[j] = l1[j] % 10  # +5之后的数字对10取余数存入该列表
# print(l1)
l1.reverse()  # 翻转列表
# print(l1)
for i in l1:
    print(i, end='')  # 加密之后输出
