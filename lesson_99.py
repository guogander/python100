# 题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。

A = open('files/A.txt', 'r', encoding='utf-8')  # 只读方式打开
s1 = A.readline()  # 读取第一行整行
B = open('files/B.txt', 'r', encoding='utf-8')
s2 = B.readline()
s3 = sorted(s1 + s2)  # 将字符串排序=并返回列表
with open('files/C.txt', 'w', encoding='utf-8') as C:  # 写入
    C.writelines(s3)   # writelines()向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。不必遍历列表一个个写入
    # for i in s3:
    #     C.write(i)
A.close()
B.close()
