# 题目：输出指定格式的日期。
import time
import datetime
# 获取当前时间
print(time.localtime())

print(datetime.date.today())
# 输入时间格式化输出
print(datetime.date(2021,2,2).strftime("%d/%m/%Y"))
# 时间戳获取时间
print(datetime.date.fromtimestamp(time.time()))
print(datetime.datetime.fromtimestamp(time.time()))