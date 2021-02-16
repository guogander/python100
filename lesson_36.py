# 题目：求100之内的素数。
# 参考lesson_12
# 判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。

# 当for语句中没有执行break的话，遍历完for语句，就会执行else语句,但是如果中间执行了break语句，跳出for循环，那么不会执行else语句。
# for全部执行完,才会执行else

for num in range(1, 101):
    if num > 1:      # 素数大于 1
        for i in range(2, num):  # 2没有进循环,执行else
            if (num % i) == 0:
                break
        else:
            print(num)
