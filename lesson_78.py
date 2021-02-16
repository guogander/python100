# 题目：找到年龄最大的人，并输出。请找出程序中有什么问题。

# 实例代码
if __name__ == '__main__':
    person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
    m = 'li'  # 假设最大值得键是第一个
    for key in person.keys():   # keys获取字典的键
        if person[m] < person[key]:
            m = key  # 交换最大值

    print('%s,%d' % (m, person[m]))

# a = {'a':1,'b':3}
# a.items()  # 获取键值,并返回迭代器
# print(a)
# for k,v in a.items():
#     print(k,v)

