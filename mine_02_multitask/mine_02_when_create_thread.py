import time
import threading


def test1():
    for i in range(5):
        print("----test1-----%d" % i)
        time.sleep(1)


# 结论：
# threading.Thread(target=test1) 仅仅创建了个对象，并没有创建一个子线程
# 只有在t1.start()之后才会创建一个子线程，并且让子线程开始运行
def main():
    print(threading.enumerate())
    t1 = threading.Thread(target=test1)
    print(threading.enumerate())
    t1.start()
    print(threading.enumerate())


if __name__ == '__main__':
    main()
