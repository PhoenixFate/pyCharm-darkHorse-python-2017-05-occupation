# 使用yield完成多任务
# 使用协程完成多任务
import time


def task1():
    while True:
        print("task1")
        time.sleep(0.2)
        # yield 的作用是是函数暂停，并可以通过 next() 来调用
        yield


def task2():
    while True:
        print("task2")
        time.sleep(0.2)
        yield


def main():
    t1 = task1()
    t2 = task2()
    # 协程的消耗资源很少
    while True:
        next(t1)
        next(t2)


if __name__ == '__main__':
    main()
