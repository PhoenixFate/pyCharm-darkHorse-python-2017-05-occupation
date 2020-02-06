# socket 套接字

import socket


def main():
    print("socket 基本使用")
    # 创建一个udp docket
    # 第一个参数，指定ipV4还是 ipV6
    # 第二个参数，指定udp还是tcp类型的socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 目标地址
    dest_addr = ("127.0.0.1", 8099)

    # 自己的程序，如果不指定端口，会随机分配一个端口
    # 手动绑定端口端口
    udp_socket.bind(("", 7899))
    while True:
        # 可以使用套接字 接受发送数据
        # udp_socket.sendto("msg","对方的ip和port")
        send_data = input("请输入要发送的数据(exit退出程序)：")
        if send_data == "exit":
            break
        udp_socket.sendto(send_data.encode("utf-8"), dest_addr)

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
