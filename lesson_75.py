# 题目：放松一下，算一道简单的题目。


if __name__ == '__main__':
    for i in range(5):
        n = 0
        if i != 1: n += 1
        if i == 3: n += 1
        if i == 4: n += 1
        if i != 4: n += 1
        if n == 3: print(64 + i)
# 分析:
# i=0 n=0 --> 到达第一个if n=1 i=0 --> 到达第四个if n=2 i=0 第0个循环结束
# i=1 n=0 --> 到达第四个if n=1 第1个循环结束
# i=2 n=0 --> 到达第一个if n=1 i=2 --> 到达第四个if n=2 i=2 第2个循环结束
# i=3 n=0 --> 到达第二个if n=1 i=3 --> 到达第四个if n=3 i=3 --> 到达第五个if i=3 打印67  第3个循环结束
# i=4 n=0 --> 到达第一个if n=1 i=4 --> 到达第三个if n=2 i=4 第4个循环结束
# i=5 n=0 --> 到达第一个if n=1 i=5 第5个循环结束
# 打印67
