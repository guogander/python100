# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# https://www.runoob.com/python/python-strings.html
s = input("随便输入:")
eng = 0
space = 0
digit = 0
others = 0
for i in s:
    if i.isalpha():  # 判断字母
        eng += 1
    elif i.isspace():  # 判断空格
        space += 1
    elif i.isdigit():  # 判断数字
        digit += 1
    else:
        others += 1
print("英文字母有%d个,空格有%d个,数字有%d个,其余类型有%d个." % (eng, space, digit, others))
