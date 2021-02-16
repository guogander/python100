# 题目：输入某年某月某日，判断这一天是这一年的第几天？
'''
闰年需要同时满足以下条件：
1、年份能被4整除；
2、年份若是 100 的整数倍的话需被400整除，否则是平年。
'''
year = int(input("年:"))
month = int(input("月:"))
day = int(input("日:"))
monDay = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

# 按照平年计算天数
loop = True
while loop:
    if 0 < month <= 12:
        sum = monDay[month - 1] + day
        loop = False
    else:
        print("输入错误")
        year = int(input("年:"))
        month = int(input("月:"))
        day = int(input("日:"))
# 判断是否是闰年
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    if month > 2:
        sum += 1
        print("year:%d,month:%d,day:%d\n"%(year,month,day))
        print("这一天是%d年的%d天\n"%(year,sum))
    else:
        print("year:%d,month:%d,day:%d\n" % (year, month, day))
        print("这一天是%d年的%d天\n" % (year, sum))
else:
    print("year:%d,month:%d,day:%d\n" % (year, month, day))
    print("这一天是%d年的%d天\n" % (year, sum))