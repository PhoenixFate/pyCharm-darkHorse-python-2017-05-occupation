# 进程之间的通信：Queue
from multiprocessing import Queue
from multiprocessing import Process
import multiprocessing


def download_from_web(q):
    """下载数据"""
    # 模拟从网上下载数据
    download_data = [11, 22, 33, 44]

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
    # 1.创建一个队列
    q = Queue()
    # 2.将队列的引用当作实参传递进去
    p1 = Process(target=download_from_web, args=(q,))
    p2 = Process(target=analyze_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
