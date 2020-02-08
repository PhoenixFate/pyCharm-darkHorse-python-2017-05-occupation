"""
从Python3.2开始，标准库为我们提供了concurrent.futures模块，
它提供了ThreadPoolExecutor和ProcessPoolExecutor两个类，
实现了对threading和multiprocessing的进一步抽象（这里主要关注线程池），
不仅可以帮我们自动调度线程，还可以做到：

1.主线程可以获取某一个线程（或者任务的）的状态，以及返回值。
2.当一个线程完成的时候，主线程能够立即知道。
3.让多线程和多进程的编码接口一致。
"""

from concurrent.futures import ThreadPoolExecutor
import time


# 参数times用来模拟网络请求的时间
def get_html(times):
    print("in to get_html, times:%s " % str(times))
    time.sleep(times)
    print("get page {}s finished".format(times))
    return times


def main():
    executor = ThreadPoolExecutor(max_workers=2)
    # 通过submit函数提交执行的函数到线程池中，submit函数立即返回，不阻塞
    task1 = executor.submit(get_html, 3)
    task2 = executor.submit(get_html, 2)
    task3 = executor.submit(get_html, 3)

    # done方法用于判定某个任务是否完成
    print(task1.done())
    # cancel方法用于取消某个任务,该任务没有放入线程池中才能取消成功
    print(task2.cancel())
    time.sleep(4)
    print(task1.done())
    print(task2.done())
    print(task3.done())
    # result方法可以获取task的执行结果
    print(task1.result())

    # 执行结果
    # False  # 表明task1未执行完成
    # False  # 表明task2取消失败，因为已经放入了线程池中
    # get page 2s finished
    # get page 3s finished
    # True  # 由于在get page 3s finished之后才打印，所以此时task1必然完成了
    # 3     # 得到task1的任务返回值


if __name__ == '__main__':
    main()
