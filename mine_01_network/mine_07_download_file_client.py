import socket


def main():
    # 1.创建套接字
    tcp_socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.获取服务的ip port
    dest_ip = "127.0.0.1"
    dest_port = 8766

    # 3.链接服务器
    tcp_socket_client.connect((dest_ip, dest_port))

    # 4.获取下载的文件名
    download_file_name = input("请输入要下载的文件名")

    # 5.将文件名发送到服务器
    tcp_socket_client.send(download_file_name.encode("utf-8"))

    # 6.接受文件中的数据
    receive_data = tcp_socket_client.recv(1024)

    # 7.保存数据到文件中
    # with 的前提是文件能够打开，read/write的时候 如果出现异常，必定能够调用file.close()关闭文件
    if receive_data:
        with open("new_" + download_file_name, "wb") as new_file:
            new_file.write(receive_data)
    else:
        print("文件不存在")
    # 8.关闭套接字
    tcp_socket_client.close()


if __name__ == '__main__':
    main()
