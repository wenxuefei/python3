from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

# 创建UDP套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)

# 绑定一个端口
udp_socket.bind(('', 8989))  # 绑定本机，端口为8989


# # 键盘接收发送的信息】
# data = input('请输入要发送的信息')
#
# # 调用sendto 方法发送信息
# udp_socket.sendto(data.encode('gb2312'), addr)
#
# # 接收数据
# recv_data = udp_socket.recvfrom(1024)  # 本次接收的最大字节数
# print('接收到%s的消息是%s' % (recv_data[1], recv_data[0].decode('gb2312')))
# # 关闭套接字
# udp_socket.close()

# udp 实现多线程聊天

# 接收消息
def recv_fun():
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print('>>%s:%s' % (recv_data[1], recv_data[0].decode('gb2312')))


# 发送消息
def send_func():
    while True:
        # 创建接收信息的地址
        addr = ('192.168.3.158', 8088)
        data = input('<<:')
        udp_socket.sendto(data.encode('gb2312'), addr)


if __name__ == '__main__':
    # 创建两个线程
    p1 = Thread(target=send_func)
    p2 = Thread(target=recv_fun)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
