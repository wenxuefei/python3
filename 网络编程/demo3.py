from socket import *

# 创建套接字对象
serverSocket = socket(AF_INET, SOCK_STREAM)

# 绑定端口
serverSocket.bind(('', 9999))

# 监听
serverSocket.listen()

# 接收客户端的链接
client_socket, client_info = serverSocket.accept()

while True:
    # 接收客户端发送的消息
    rect_data = client_socket.recv(1024)
    print('客户端说：', rect_data.decode('utf-8'))
    # print('接收到%s的消息%s' % (client_info, rect_data.decode('gb2312')))
    if rect_data.decode('utf-8') == 'bye':
        break
    # 发送消息
    msg = input('>')
    client_socket.send(msg.encode('utf-8'))
# 关闭链接
client_socket.close()
serverSocket.close()
