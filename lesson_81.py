# 题目：809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。
for i in range(10, 100):
    if 999 < 809 * i < 10000 and 9 < 8 * i < 100 and 99 < 9 * i < 1000:
        print("??代表的数是%d,809*??既为809*%d = %d" % (i, i, 809 * i))