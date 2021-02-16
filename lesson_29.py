# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
s = input("请输入不多于五位的正整数:")

n = []
for i in range(5):
    n.append(int(s[i]))  # 为了严谨,将字符串转为整型
n.reverse()  # 翻转序列
print(n)
for i in n:
    print(i)