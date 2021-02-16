# 题目：时间函数举例1。
# https://blog.csdn.net/qq_27283619/article/details/89280974

if __name__ == '__main__':
    import time
    print(time.time())  # 获取时间戳
    print(time.localtime())  # 获取当前时间   tm_wday=0   0-6 0是周一; tm_yday=39   1 到 366(儒略历); tm_isdst=0    -1, 0, 1, -1是决定是否为夏令时的旗帜
    print(time.ctime(time.time()))  # 没有返回值,作用是:把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式
    print(time.asctime(time.localtime(time.time())))  # 返回一个可读的形式为"Mon Feb  8 20:51:32 2021"的24个字符的字符串。
    print(time.asctime(time.gmtime(time.time())))   # time.gmtime(time.time())没有返回值:将一个时间戳转换为UTC时区（0时区）的struct_time


