# 题目：列表转换为字典。
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
a = [1, 2, 3, 2]  # 键名重复的话,后面的值会覆盖前面的值
b = [4, 5, 6, 7]
c = zip(a, b)
# print(list(c))
# for i in c:
#     print(i)
print(dict(c))  # 如果经过上面的list(c)或者遍历之后,下面的字典就是空
