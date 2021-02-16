# 题目：画图，学用line画直线。

# # 画一个四边颜色不同的正方形,边长100
# import turtle
# pen = turtle.Turtle()  # 定义画笔
# turtle.colormode(255)  # 定义画笔颜色模式
# pen.pensize(5)  # 设置画笔大小
# color = ['yellow', 'green', 'blue', 'red']
# for i in range(4):
#     pen.color(color[i])
#     pen.forward(100)
#     # 每次循环都在上次循环基础转90度
#     pen.left(90)
# turtle.done()

if __name__ == '__main__':
    from tkinter import *

    canvas = Canvas(width=500, height=500, bg='green')
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_line(120, 100, 150, 150)  # 四个数值表示直线的两个端点坐标
    canvas.create_line(100, 100, 150, 150)
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_line(x0, y0, x0, y1, width=1, fill='red', dash=(4, 4))  # dash 虚线
        x0 = x0 - 5
        y0 = y0 - 5
        x1 = x1 + 5
        y1 = y1 + 5

    x0 = 263
    y1 = 275
    y0 = 263
    for i in range(21):
        canvas.create_line(x0, y0, x0, y1, fill='red')
        x0 += 5
        y0 += 5
        y1 += 5

    mainloop()
