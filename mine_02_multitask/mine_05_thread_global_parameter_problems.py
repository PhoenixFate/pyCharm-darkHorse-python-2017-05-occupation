import threading
import time

g_num = 0


def work1():
    global g_num

    for i in range(100000):
        g_num += 1


def work2():
    global g_num

    for i in range(100000):
        g_num += 1


def main():
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)
    t1.start()
    t2.start()

    time.sleep(2)
    print(g_num)


if __name__ == '__main__':
    main()
