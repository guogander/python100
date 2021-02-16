# 题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

# 定义输入函数,保存到序列
def inp(arr):
    for i in range(6):
        a = int(input("输入数字:"))
        arr.append(a)


# 最大的换到第一个
def ex_max(arr):
    max = 0  # 假设最大为第一个
    for i in range(1, 5):
        if arr[i] > arr[max]:  # 找出最大的数的索引值
            max = i
    arr[0], arr[max] = arr[max], arr[0]


# 最小的换到最后
def ex_min(arr):
    min = 5  # 假设最小为最后一个
    for i in range(1, 5):
        if arr[i] < arr[min]:  # 找出最小的数的索引值
            min = i
    arr[5], arr[min] = arr[min], arr[5]


arr = []
inp(arr)
ex_max(arr)
ex_min(arr)
print(arr)


# 直接利用max,min内置函数求的最大最小数
a = [1, 2, 3, 7, 9, 8]
for i in range(len(a)):
    if a[i] == max(a):
        a[0], a[i] = a[i], a[0]

for i in range(len(a)):
    if a[i] == min(a):
        a[len(a) - 1], a[i] = a[i], a[len(a) - 1]

print(a)
