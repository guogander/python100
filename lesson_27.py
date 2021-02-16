# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
str = list(input("请输入五个字符:"))

def string(s):
    if len(s) == 1:
        print(s[len(s)-1])

    else:
        print(s[len(s) - 1])
        # s.pop()  # 默认删除最后一个元素
        del str[-1]  # 删除最后一个元素 这两个都是list的方法,需要将字符串转为list
        string(s)

string(str)

# def desc_output(s):
#     if(len(s) > 0):
#         print(s[-1])            # python 负数下标
#         desc_output(s[0:-1])  # -1表示最后一个元素索引,但是切片包左不包右就删掉了最后一个元素
#
# s = input('Input a string:')
# desc_output(s)