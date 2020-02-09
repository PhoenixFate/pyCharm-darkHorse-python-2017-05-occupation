# 使用greenlet 完成：协程多任务
# python 默认没有greenlet
# sudo pip/pip3 install greenlet

from greenlet import greenlet
import time


def task1():
    while True:
        print("--- task1 ---")
        greenlet2.switch()
        time.sleep(1)


def task2():
    while True:
        print("--- task2 ---")
        greenlet1.switch()
        time.sleep(1)


greenlet1 = greenlet(task1)
greenlet2 = greenlet(task2)


def main():
    greenlet1.switch()


if __name__ == '__main__':
    main()
