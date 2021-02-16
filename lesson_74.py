# 题目：列表排序及连接。
# 使用sort  "+"或extend()


# 排序
a = [9, 6, 1, 12, 2, 8, 3, 4]
print("排序前:", a)
a.sort()
print("排序后:", a)

# 连接
b = [1, 2, 3]
c = [4, 5, 6]
d = b + c
b.extend(c)  # extend 会修改原序列,将列表c添加在列表b后面,没有返回值
print("+连接:", d)
print("extend拼接:", b)
