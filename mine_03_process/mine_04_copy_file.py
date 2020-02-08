import os
import time
import random
from multiprocessing import Pool
import multiprocessing


def copy_file(file_queue, file_name, old_dir_name, new_dir_name):
    """完成文件的复制"""
    # print("==> 拷贝文件名: 从%s 到%s, 文件名: %s" % (old_dir_name, new_dir_name, file_name))
    old_file = open(old_dir_name + "/" + file_name, "rb")
    new_file = open(new_dir_name + "/" + file_name, "wb")
    while True:
        time.sleep(random.random() * 2)
        content = old_file.read(1024)
        if content:
            new_file.write(content)
        else:
            break
    old_file.close()
    new_file.close()

    # 发送已经拷贝完成的文件名字
    file_queue.put(file_name)


def main():
    # 1.获取用户要copy的文件夹名字
    old_dir_name = input("请输入要copy的文件夹名字: ")

    new_dir_name = old_dir_name + "_copy"
    # 2.创建一个新的文件夹
    try:
        # 存在则不创建
        os.mkdir(new_dir_name)
    except Exception as e:
        print(e)
        pass

    # 3.获取文件架的所有待copy的的文件名 file_names
    file_names = os.listdir(old_dir_name)
    print(file_names)
    # 4.创建进程池
    file_pool = Pool(3)

    # 创建队列
    file_queue = multiprocessing.Manager().Queue()

    # 5.向进程池中添加copy文件的任务
    for file_name in file_names:
        file_pool.apply_async(copy_file, (file_queue, file_name, old_dir_name, new_dir_name))

    # 复制原文件夹的文件，到新文件夹下面
    file_pool.close()
    # file_pool.join()

    # 所有文件总数
    all_file_num = len(file_names)
    copy_ok_num = 0
    while True:
        # 显示进度
        finished_flie_name = file_queue.get()
        copy_ok_num += 1
        print("\r拷贝进度：%.2f %%" % (copy_ok_num / all_file_num * 100), end="")
        if copy_ok_num >= all_file_num:
            print()
            break


if __name__ == '__main__':
    main()
