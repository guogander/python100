# 题目：编写input()和output()函数输入，输出5个学生的数据记录。

# num : string
# name : string
# score[4] : list
N = 3  # 设置学生数量


# 输入数据
def input_stu(stu):
    # 输入学生
    for i in range(N):  # N个学生
        stu[i][0] = input("输入学号:")
        stu[i][1] = input("输入姓名:")
        for j in range(4):  # 登记分数,四门分数
            # stu[i][2] = int(input("输入分数:"))
            stu[i][2].append(int(input("输入分数:")))  # 将输入的数据直接添加到列表中的空列表中
            # 四门成绩也可单独输出stu[i][2][j]  j为下一个循环的索引


# 输出数据
def output_stu(stu):
    for i in range(N):
        print("%s学号是:%s,他的各项成绩为(语文/数学/英语/综合):%s" % (stu[i][1], stu[i][0], stu[i][2]))


if __name__ == '__main__':
    # 创建学生列表
    stu = []
    for i in range(N):
        stu.append(['', '', []])
    # stu = [['01', 'gg', [69, 98, 65, 68]], ['02', 'hh', [98, 95, 68, 59]], ['03', 'rr', [98, 97, 54, 23]]]  # 预先设定数据
    input_stu(stu)
    output_stu(stu)
    # print(stu)
