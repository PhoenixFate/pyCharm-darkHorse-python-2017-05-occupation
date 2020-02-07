# thread是底层模块，使用不方便
# threading是在thread模块上封装的模块，使用更方便
import time
import threading


def sing():
    """唱歌"""
    for i in range(5):
        print("正在唱歌: %d" % i)
        time.sleep(1)


def dance():
    """跳舞"""
    for i in range(5):
        print("正在跳舞: %d" % i)
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)

    # 多个子线程的执行先后顺序 并不确定
    t1.start()
    t2.start()

    while True:
        thread_list = threading.enumerate()
        print(thread_list)
        length = len(thread_list)
        print("当前运行的线程数量 %d " % length)
        if length <= 1:
            break

        time.sleep(0.5)


if __name__ == '__main__':
    main()
