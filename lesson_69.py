# 题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

n = int(input("n:"))
a = []
# 创建n个人的列表,1开始排序
for i in range(n):
    a.append(i + 1)
print(a)
j = 1
while len(a) > 1:
    # 每循环一次就删除第一个数字,如果不是3的倍数,就删完之后将其移到最后面
    if j % 3 == 0:  # j 进行循环,一旦满足3的倍数就进行删除
        a.pop(0)  # 删除列表第一个元素
    else:
        a.insert(len(a), a.pop(0))  # 不满足3的倍数的删除之后添加到列表最后,相当于挪位置
    j += 1  # 自增
print(a)