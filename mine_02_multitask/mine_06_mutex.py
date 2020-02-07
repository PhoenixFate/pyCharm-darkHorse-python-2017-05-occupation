# 互斥锁
import threading
import time

g_num = 0

# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()


def work1():
    global g_num
    # 上锁，如果之前没有被上锁，那么此时上锁成功
    # 如果上锁之前 已经被上锁了，那么此时会堵塞在这里，直到这个锁被解开
    mutex.acquire()
    for i in range(100000):
        g_num += 1
    # 解锁
    mutex.release()
    print("work1 g_num: %d" % g_num)


def work2():
    global g_num
    # 谁先上锁 先执行
    mutex.acquire()
    for i in range(100000):
        g_num += 1
    mutex.release()
    print("work2 g_num: %d" % g_num)


def main():
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)
    t1.start()
    t2.start()

    time.sleep(2)
    print(g_num)


if __name__ == '__main__':
    main()
