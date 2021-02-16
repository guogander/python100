# 题目：模仿静态变量的用法。
def varfunc():
    var = 0
    print(var)
    var += 1  # 实际上这行没有意义,每次进入这个函数都会被置0


for i in range(3):
    varfunc()

print("-----------分割线------------")


# 定义一个类
class Val:
    staticVar = 5

    def var(self):
        self.staticVar += 1
        print(self.staticVar)

    def m(self):
        self.var()


# 创建实例
a = Val()
print(a.staticVar)
for i in range(3):
    a.var()
# print(a.staticVar)
a.m()
