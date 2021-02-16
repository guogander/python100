# 题目：时间函数举例2。

if __name__ == '__main__':
    import time

    # time.process_time()  返回当前进程的系统和用户CPU时间总和的值（以小数秒为单位）作为浮点数。process_time()不包括sleep()休眠时间期间经过的时间。
    start = time.process_time()
    for i in range(3000):
        print(i)
    end = time.process_time()

    print(end - start)

    # time.perf_counter()会包含sleep()休眠时间，适用测量短持续时间
    start = time.perf_counter()
    for i in range(3000):
        print(i)
    end = time.perf_counter()
    print(end - start)