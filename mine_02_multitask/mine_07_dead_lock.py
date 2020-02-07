import threading
import time

mutexA = threading.Lock()
mutexB = threading.Lock()


class MyThread1(threading.Thread):
    def run(self) -> None:
        # 对mutexA上锁
        mutexA.acquire()

        # mutexA上锁之后，延迟1秒，等待另一个线程mutexB上锁
        print(self.name + "----------do1------up")
        time.sleep(1)

        # 此时会堵塞，因为这个mutexB已经被另外的线程抢先上锁了
        mutexB.acquire()
        print(self.name + "----------do1------up")
        mutexB.release()

        # 对mutexA解锁
        mutexA.release()


class MyThread2(threading.Thread):
    def run(self) -> None:
        # 对mutexB上锁
        mutexB.acquire()

        print(self.name + "------------do2-------up")
        time.sleep(1)

        mutexA.acquire()
        print(self.name + "------------do2------down")
        mutexA.release()

        mutexB.release()


def main():
    t1 = MyThread1()
    t2 = MyThread2()

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
