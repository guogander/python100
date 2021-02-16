# 题目：利用递归方法求5!。
def jiecheng(n):
    s = n
    if n == 1:
        return s
    else:
        return s * jiecheng(n - 1)


s = jiecheng(5)
print(s)
