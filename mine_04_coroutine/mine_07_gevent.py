# 使用gevent 完成协程多任务
# pip install gevent
# gevent 遇到延时操作 就切换
import gevent
import time


def test01(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(1)
        # 遇到延时则切换线程
        gevent.sleep(1)


def test02(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(1)
        # 遇到延时则切换线程
        gevent.sleep(1)


def test03(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(1)
        # 遇到延时则切换线程
        gevent.sleep(1)


g1 = gevent.spawn(test01, 5)
g2 = gevent.spawn(test02, 5)
g3 = gevent.spawn(test03, 5)
# 耗时的时候 启动切换
# g1.join()
# g2.join()
# g3.join()
