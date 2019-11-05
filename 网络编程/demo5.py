from socket import *
from threading import Thread

sockets = []


# 服务器端
def main():
    # 创建server_socket 套接字对象
    server_socket = socket(AF_INET, SOCK_STREAM)
    # 绑定端口
    server_socket.bind(('', 7878))
    # 监听
    server_socket.listen()
    # 接收客户端的请求
    while True:
        client_socket, client_info = server_socket.accept()
        sockets.append(client_socket)
        # 开启线程处理当前客户端的请求
        t = Thread(target=readMsg, args=(client_socket,))


def readMsg(client_socket):
    # 读取客户端发送来的消息
    while True:
        recv_data = client_socket.recv(1024)
        # 将消息发送给所有在线的客户端
        # 遍历所有在线客户端列表
        for i in sockets:
            print(i)
            i.send(recv_data)


if __name__ == '__main__':
    main()
