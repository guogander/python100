# 题目：画图，学用rectangle画方形。

# rectangle(int left, int top, int right, int bottom)
# 参数说明：(left ，top )为矩形的左上坐标，(right,bottom)为矩形的右下坐标，两者可确定一个矩形的大小
if __name__ == '__main__':
    from tkinter import *

    root = Tk()  # 创建窗口
    root.title('正方形')  # 窗口标题
    canvas = Canvas(root, width=400, height=400, bg='yellow')  # 设置属性
    x0 = 263
    y0 = 263
    y1 = 275
    x1 = 275
    for i in range(19):
        canvas.create_rectangle(x0, y0, x1, y1)  # 矩形的左上坐标和右下坐标
        x0 -= 5
        y0 -= 5
        x1 += 5
        y1 += 5

    canvas.pack()
    root.mainloop()  # 使程序停留