# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
n = int(input("请输入一个数:"))
a.append(n)
print(a)
a.sort()
print(a, end="\n\n\n\n\n\n")

a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100, 0]  # 0是占位
print(a)
number = int(input("插入一个数字:"))
end = a[9]  # 最后一个数字
if number > end:
    a[10] = number
else:
    for i in range(10):
        if number < a[i]:
            t1 = a[i]  # 将被替换的数字存起来
            a[i] = number  # 判断这个数是否小于某个数,小于就替换当前位置
            for j in range(i + 1, 11):  # 然后将后面的数字都向后推移一位
                t2 = a[j]  # 后面将要被替换的数字存起来
                a[j] = t1  # 将之前存起来的数字放在后面一位
                t1 = t2  # 将现在的数字又存起来,之后重复
            break  # 替换完一轮之后直接结束循环不再继续比较
print(a)
