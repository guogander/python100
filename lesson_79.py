# 题目：字符串排序。
a = 'fgagfsdg'
b = 'fgagyryr'
c = 'agsdfgdd'
print(a,b,c)
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a,b,c)