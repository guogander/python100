# 题目：从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
# upper()将字符串中的小写转换为大写
# lower()转换字符串中所有大写字符为小写.
# swapcase()将字符串中大写转换为小写，小写转换为大写
with open('files/text.txt', 'a', encoding='utf-8') as f:
    s1 = input('字符串1:')
    s2 = input('字符串2:')
    s3 = input('字符串3:')
    s1 = s1.upper()
    s2 = s2.lower()
    s3 = s3.swapcase()
    f.write(s1+'\n')
    f.write(s2+'\n')
    f.write(s3+'\n')