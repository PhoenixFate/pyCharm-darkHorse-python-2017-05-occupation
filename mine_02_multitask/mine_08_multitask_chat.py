import threading
import socket


def receive_message(udp_socket):
    """接受数据"""
    while True:
        receive_data = udp_socket.recvfrom(1024)
        print(receive_data[0].decode("utf-8"))


def send_message(udp_socket, dest_ip, dest_port):
    """发送数据"""
    while True:
        send_data = input("请输入要发送的数据: ")
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def main():
    """完成udp聊天器的整体控制"""

    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定本地信息
    local_address = ("", 8699)
    udp_socket.bind(local_address)

    # 3.对方的ip和port
    dest_ip = "127.0.0.1"
    dest_port = 8799

    # 创建两个线程执行相应的 接受数据和发送数据
    try:
        t1 = threading.Thread(target=receive_message, args=(udp_socket,))
        t2 = threading.Thread(target=send_message, args=(udp_socket, dest_ip, dest_port))
        t1.start()
        t2.start()
    except Exception as e:
        print(e)
    # finally:
    #     udp_socket.close()


if __name__ == '__main__':
    main()
