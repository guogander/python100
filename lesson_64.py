# 题目：利用ellipse 和 rectangle 画图。
from tkinter import *
root = Tk()
canvas = Canvas(root,width = 1000,height = 1000)
canvas.pack()

# 矩形
x0 = 100
y0 = 100
x1 = 150
y1 = 150
for i in range(20):
    canvas.create_rectangle(x0, y0, x1, y1)
    x0 -= 5
    y0 -= 5
    x1 += 10
    y1 += 10

# 椭圆
x0 = 300
y0 = 300
x1 = 700
y1 = 700
for i in range(30):
    canvas.create_oval(x0, y0, x1, y1)   # 由圆变为椭圆,左上角x0↑y0↓,右下角x1↓y1↑,x轴变化慢一些,y变化快一些
    x0 += 5
    x1 -= 5
    y0 -= 10
    y1 += 10

mainloop()