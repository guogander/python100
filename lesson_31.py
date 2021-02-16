# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
s = input("请输入星期几的首大写字母:")
if s == 'M':
    print("M表示是星期一!")
elif s == 'W':
    print("W表示是星期三!")
elif s == 'F':
    print("F表示是星期五!")
elif s == 'T':
    s = input("请输入第二个字母(小写):")
    if s == 'u':
        print("Tu表示是星期二!")
    elif s == 'h':
        print("Th表示是星期四!")
    else:
        print("输入错误!")
elif s == 'S':
    s = input("请输入第二个字母(小写):")
    if s == 'a':
        print("Sa表示是星期六!")
    elif s == 'u':
        print("Su表示是星期四!")
    else:
        print("输入错误!")
else:print("输入错误!")
