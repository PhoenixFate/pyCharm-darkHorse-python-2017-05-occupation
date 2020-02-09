# mine_07_gevent 需要使用gevent.sleep()，并且其他延时操作需要换用gevent里面的模块，
# 使用使用另一种方式使用gevent

from gevent import monkey
import gevent
import random
import time

# 有耗时任务需要
monkey.patch_all()


def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(random.random() * 2)


gevent.joinall([
    gevent.spawn(coroutine_work, "work1"),
    gevent.spawn(coroutine_work, "work2")
])
