# 题目：一个最优美的图案。　
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import math
# class PTS:
#     def __init__(self):
#         self.x = 0
#         self.y = 0
# points = []
#
# from tkinter import *
# def LineToDemo():
#     screenx = 400
#     screeny = 400
#     canvas = Canvas(width = screenx,height = screeny,bg = 'white')
#
#     AspectRatio = 0.85
#     MAXPTS = 15
#     h = screeny
#     w = screenx
#     xcenter = w / 2
#     ycenter = h / 2
#     radius = (h - 30) / (AspectRatio * 2) - 20
#     step = 360 / MAXPTS
#     angle = 0.0
#     for i in range(MAXPTS):
#         rads = angle * math.pi / 180.0
#         p = PTS()
#         p.x = xcenter + int(math.cos(rads) * radius)
#         p.y = ycenter - int(math.sin(rads) * radius * AspectRatio)
#         angle += step
#         points.append(p)
#     canvas.create_oval(xcenter - radius,ycenter - radius,
#                        xcenter + radius,ycenter + radius)  # 画圆
#     for i in range(MAXPTS):
#         for j in range(i,MAXPTS):
#             canvas.create_line(points[i].x,points[i].y,points[j].x,points[j].y)  # 画线
#
#     canvas.pack()
#     mainloop()
# if __name__ == '__main__':
#     LineToDemo()


# 绘制一棵分型树：来源:廖雪峰网站

from turtle import *

# 设置色彩模式是RGB:
colormode(255)

lt(90)

lv = 14
l = 120
s = 45

width(lv)

# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)

speed("fastest")

draw_tree(l, 4)

done()