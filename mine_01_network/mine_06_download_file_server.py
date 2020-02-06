import sys
import socket


def get_file_context(file_name):
    try:
        file = open(file_name, "rb")
        file_data = file.read()
        file.close()
        return file_data
    except Exception as e:
        print(e)
        return None


def main():
    if len(sys.argv) != 2:
        port = 8766
        print("请按照如下命令运行：python3 xxx.py 8096, 默认端口：%d" % port)
    else:
        port = int(sys.argv[1])

    # 创建socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 本地信息
    local_address = ("", port)
    tcp_server_socket.bind(local_address)

    # 让默认的socket主动变被动listen
    tcp_server_socket.listen(128)

    # 等待客户端链接
    client_socket, client_address = tcp_server_socket.accept()

    # 接受客户端发送过来的文件名
    download_file_name = client_socket.recv(1024).decode("utf-8")
    print("客户端%s 需要下载的文件名：%s" % (str(client_address), download_file_name))

    # 读取文件内容
    # 发送数据给客户端
    file_data = get_file_context(download_file_name)
    if file_data:
        client_socket.send(file_data)

    # 关闭套接字
    client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
