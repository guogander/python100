# 题目：反向输出一个链表。
l1 = [int(input("please input a number:\n")) for i in range(5)]
l2 = l1[::-1]

l1.reverse()
print(l1)
print(l2)
for i in range(len(l2)):
    print(l2[i])