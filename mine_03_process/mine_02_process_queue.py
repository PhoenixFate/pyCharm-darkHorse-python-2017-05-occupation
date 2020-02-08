# 进程之间的通信：Queue
from multiprocessing import Queue
from multiprocessing import Process
import multiprocessing
import time


def basic_usage():
    q = Queue(3)
    print("q.empty(): %s" % q.empty())
    q.put("message1")
    q.put("message2")
    print("q.full(): %s" % q.full())
    q.put("message3")
    print("q.full(): %s" % q.full())

    try:
        q.put("message4", True, 2)
    except Exception as e:
        print(e)
        print("queue已经满了：%s" % q.qsize())

    try:
        q.put_nowait("message5")
    except Exception as e:
        print(e)
        print("queue已经满了：%s" % q.qsize())

    print(q.get())

    if not q.full():
        q.put("message7")


def download_from_web(q):
    """下载数据"""
    # 模拟从网上下载数据
    download_data = [11, 22, 33, 44]
    time.sleep(1)
    # 向队列中写入数据
    q.put(download_data)

    print("下载完数据")


def analyze_data(q):
    """数据处理"""
    analyze_temp_data = list()
    # 从队列中获取数据
    while True:
        temp_data = q.get()
        analyze_temp_data.append(temp_data)
        if q.empty():
            break

    print(analyze_temp_data)


def main():
    basic_usage()

    # 1.创建一个队列
    q = Queue()
    # 2.将队列的引用当作实参传递进去
    p1 = Process(target=download_from_web, args=(q,))
    p2 = Process(target=analyze_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
