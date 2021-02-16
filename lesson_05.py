# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

if x < y:
    x, y = y, x
else:
    if x < z:
        x, z = z, x
    else:
        if y < z:
            y, z = z, y
print(z,y,x)
# 可以直接内置函数sort()列表排序