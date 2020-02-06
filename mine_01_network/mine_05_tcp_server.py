import socket


def main():
    # 创建socket
    tcp_sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("tcp 服务器已经启动")

    # 绑定本地信息
    local_address = ("127.0.0.1", 8799)
    tcp_sever_socket.bind(local_address)

    # 使用socket创建的套接字默认是主动的，使用listen将其变成被动，这样就可以接受别人的链接了
    tcp_sever_socket.listen(128)

    # 循环为多个客户端 服务
    while True:
        print("等待一个客户端到来")
        # 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务
        # client_socket用来为这个客户端服务
        # tcp_sever_socket就可以省下来专门等待其他新客户端的链接
        client_socket, client_address = tcp_sever_socket.accept()
        print("一个新的客户端已经到来：%s" % str(client_address))

        # 循环接受多次消息
        while True:
            # 接受对方发送过来的数据
            receive_data = client_socket.recv(1024)
            print("接受到的数据：%s" % receive_data.decode("utf-8"))

            # 如果receive_data解堵塞，那么有两种方式：
            # 1.客户端发送过来数据
            # 2.客户端调用close，导致receive_data解堵塞，并且receive_data是空
            if receive_data:
                # 有数据
                # 发送一些数据到客户端
                client_socket.send("tcp 服务器 响应成功".encode("utf-8"))
            else:
                # 没数据，客户端调用close
                break

        # 关闭为这个客户端服务到套接字，只要关闭了，就意味着不能再为这个客户端服务了
        print("结束服务")
        client_socket.close()

    tcp_sever_socket.close()


if __name__ == '__main__':
    main()
