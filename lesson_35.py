# 题目：文本颜色设置。
# 参考这篇文章 https://blog.51cto.com/guyuyuan/1920615

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[101m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("\033[1;31;40m你查查")
print(bcolors.HEADER + "警告的颜色字体?")
print(bcolors.WARNING + "警告的颜色字体?")
