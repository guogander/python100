# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
sorce = int(input("请输入分数:"))
if 90 <= sorce <= 100:
    print("A")
elif 60 <= sorce <= 89:
    print("B")
elif 60 > sorce >= 0:
    print("C")
else:
    print("输入有误!")