from multiprocessing import Pool
import os
import time
import random


def worker(message):
    t_start = time.time()
    print("%s开始执行, 进程号为:%d" % (message, os.getpid()))
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(message, "执行完毕，耗时：%.2f" % (t_stop - t_start))


def main():
    # 定义一个进程池，最大进程数3
    process_pool = Pool(3)
    for i in range(10):
        # Pool.apply_async(要调用的目标,(传递给目标的参数元组,)
        # 每次循环将会空闲出来的子进程去调用目标
        process_pool.apply_async(worker, (i,))

    print("--- start ---")
    # 关闭进程池子，关闭后，process_pool不再接受新的请求
    process_pool.close()
    # 等待process_pool中所有子进程结束，必须放在close之后
    # 默认，通过线程池创建的子进行，主进程不等待
    process_pool.join()
    print("--- end ---")


if __name__ == '__main__':
    main()
