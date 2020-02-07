import threading
import time

g_num = 100
g_nums = [12, 2323]


# 多线程共享全局变量
def work1(temp_nums):
    global g_num
    temp_nums.append(33)
    # 在一个函数中 对全局变量进行修改的时候，到底是否需要使用global修饰 需要看是否对全局变量的指向进行修改
    # 如果修改了指向，必须使用global关键字
    # 如果仅仅修改指向中的内存的值，可以不用global
    g_nums.append(23)
    for i in range(3):
        g_num += 1
    print("in work1, global num is: %d" % g_num)
    print("temp_nums: %s " % str(temp_nums))


def work2(temp_nums):
    global g_num
    print("in work2, globam num is: %d" % g_num)
    print("temp_nums: %s" % str(temp_nums))


def main():
    # target 指定将来这个线程要去哪个函数执行代码
    # args 指定调用函数时 传递的参数
    # args=() 里面必须是一个元祖
    t1 = threading.Thread(target=work1, args=(g_nums,))
    t1.start()

    # 延迟一会，保证t1中的任务全部跑完
    time.sleep(1)

    t2 = threading.Thread(target=work2, args=(g_nums,))
    t2.start()


if __name__ == '__main__':
    main()
