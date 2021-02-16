# 题目：字符串日期转换为易读的日期格式。
import time

localTime = time.localtime()
formatTime = time.strftime('Y%-m%-d% H%:M%:S%', localTime)
print(localTime)
print(formatTime)
