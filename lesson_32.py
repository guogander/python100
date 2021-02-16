# 题目：按相反的顺序输出列表的值。
s1 = ['a','b','c','d','e']
s2 = s1[::-1]  # 复制创建新的list,不改变原序列

print(s1)
print(s2)
s1.reverse()  # reverse会改变原序列
print(s1)