# 题目：模仿静态变量(static)另一案例。
class Num:
    nNum = 1

    def inc(self):
        self.nNum += 1
        print('nNum = %d' % self.nNum)


if __name__ == '__main__':
    nNum = 2  # 全局变量
    inst = Num()  # 实例化
    for i in range(3):
        nNum += 1
        print('The num = %d' % nNum)
        inst.inc()  # 第一次调用的是类里面的nNum,后两次循环由于改变了类里面的nNum所以会增加

# The num = 3,4,5
# nNum = 2,3,4
