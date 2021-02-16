# 题目：使用lambda来创建匿名函数。
#   x if x > y else y 类似于C语言的三目运算符,真返回x,假返回y

max = lambda x, y: x if x > y else y
min = lambda x, y: y if x > y else x
a = int(input("数字一:"))
b = int(input("数字二:"))

print("输入的两个数较大的是:", max(a, b))
print("输入的两个数较小的是:", min(a, b))
