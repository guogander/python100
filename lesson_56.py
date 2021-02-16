# 题目：画图，学用circle画圆形。
# import turtle
#
# # 定义画笔
# pen = turtle.Turtle()
#
# turtle.colormode(255)
# # # 让画笔前进
# # pen.forward(100)
# # # 让画笔换方向 90度
# # pen.left(90)
# # # 定义画笔的颜色,要实先声明画笔颜色模式
# # pen.color(255, 0, 0)
# # pen.forward(100)
# #
# # pen.left(90)
# # pen.forward(50)
#
# pen.color(0, 0, 255)
# # 画圆,半径50
# pen.circle(50)
#
#
# # 让屏幕暂停
# turtle.done()

from tkinter import *

if __name__ == '__main__':
    from tkinter import *

    canvas = Canvas(width=800, height=600, bg='yellow')   # 画布,声明窗口属性,宽高背景颜色
    canvas.pack(expand=YES, fill=BOTH)   # 定义窗口内容布局 fill填充属性,X,Y,BOTH
    k = 1
    j = 1
    for i in range(0, 26):
        canvas.create_oval(500 - k, 400 - k, 500 + k, 400 + k, width=1)  # 画圆  前面四项表示圆外矩形左上角与右下角坐标   width定义线的粗细
        k += j
        j += 1

    mainloop()  # 执行整个函数
