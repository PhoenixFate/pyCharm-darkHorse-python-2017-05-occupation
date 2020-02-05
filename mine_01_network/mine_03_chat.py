import socket


def send_message(udp_socket):
    """发送消息"""
    dest_addr = input("请输入你要发送的地址:")
    dest_port = int(input("请输入你要发送的端口:"))
    # 获取要发送的内容
    send_data = input("请输入你要发送的数据:")
    udp_socket.sendto(send_data.encode("utf-8"), (dest_addr, dest_port))


def receive_message(udp_socket):
    """接受消息"""
    receive_data = udp_socket.recvfrom(1024)
    print("接受到 %s 的数据：%s" % (str(receive_data[1]), receive_data[0].decode("utf-8")))


def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定本地的信息，如果一个网络程序不绑定，则系统会随机分配
    local_addr = ("", 9099)
    udp_socket.bind(local_addr)

    # 3.while 循环来处理事情
    while True:
        print("聊天工具：")
        print("1.发送数据")
        print("2.接受数据")
        print("0.退出程序")
        choose_type = input("请输入功能:")
        if choose_type == "1":
            send_message(udp_socket)
        elif choose_type == "2":
            receive_message(udp_socket)
        elif choose_type == "0":
            break
        else:
            print("输入有误")

    udp_socket.close()


if __name__ == '__main__':
    main()
