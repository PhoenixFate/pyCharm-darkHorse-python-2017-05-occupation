import socket


def main():
    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定本地的信息，如果一个网络程序不绑定，则系统会随机分配
    local_addr = ("", 8099)
    udp_socket.bind(local_addr)

    while True:
        # 3.等待接受对方发送的消息
        receive_data = udp_socket.recvfrom(1024)  # 1024表示本次接受的最大字节数
        print(receive_data)
        # 4.显示接受到的数据
        print(receive_data[0].decode("utf-8"))

        if receive_data == "close":
            break

    # 5.关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
