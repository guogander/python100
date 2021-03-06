# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
# 注:总距离包括上去和下落,除开第一次,其余路径皆为2倍
h = 100
s = 0  # 总高度
for i in range(1,11):
    if i == 1:  # 第一次落地是单程
        s = 100
    else:  # 第二次开始是两倍高度
        h = 0.5 * h
        s += 2 * h
        if i == 10:
            print('第十次落地反弹高度为:', 0.5*h)  # 由于算总距离时,第一次下落时没有高度减半,所以实际是还要减半一次
print("总距离为:", s)
