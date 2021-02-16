# 题目：按逗号分隔列表。
L = [1, 2, 3, 4, 5]
s1 = repr(L)[1:-1]  # repr返回一个对象的 string 格式。元素之间有空格,for循环打印可以看出
for i in s1:
    print("-",i)
print(s1)

s2 = ','.join(str(n) for n in L)
print(s2)
