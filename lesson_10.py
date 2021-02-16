# 题目：暂停一秒输出，并格式化当前时间。
import time

print(time.time())  # 时间戳
print(time.localtime(time.time()))  # 格式化时间戳为本地的时间
# 优化格式化版本
print(time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime(time.time())))

# time模块访问如下
# https://www.cnblogs.com/komean/p/10603518.html