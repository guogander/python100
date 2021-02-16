# 题目：画椭圆。
from tkinter import *

root = Tk()
canvas = Canvas(root, width=1000, height=1000, bg="yellow")
canvas.pack()

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
