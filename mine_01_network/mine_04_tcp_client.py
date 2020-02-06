import socket


def main():
    # 创建tcp socket
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 目的信息
    server_ip = "127.0.0.1"
    server_port = 8799

    # 链接服务器
    tcp_client_socket.connect((server_ip, server_port))

    while True:
        send_data = input("请输入要发送到数据(exit 退出)：")
        if send_data == "exit":
            break

        # 发送消息
        tcp_client_socket.send(send_data.encode("utf-8"))

        # 接受对方发送过来的数据
        receive_data = tcp_client_socket.recv(1024)
        print("对方发送过来的数据：%s" % receive_data.decode("utf-8"))

    tcp_client_socket.close()


if __name__ == '__main__':
    main()
