import threading
import time


class MyThread(threading.Thread):

    def run(self):
        for i in range(5):
            time.sleep(1)
            print("%s : %d" % (self.name, i))


def main():
    t1 = MyThread()
    t1.start()


if __name__ == '__main__':
    main()
