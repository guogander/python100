# 计算奖金
lirun = [1000000, 600000, 400000, 200000, 100000, 0]
bili = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]

inLirun = int(input("利润为:"))
# 初始奖金
bouns = 0
for i in range(6):
    # 利润从大到小比较
    if inLirun > lirun[i]:
        bouns += (inLirun - lirun[i]) * bili[i]
        inLirun = lirun[i]
print("奖金应为:", bouns)
