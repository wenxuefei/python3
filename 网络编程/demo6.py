from socket import *
from threading import Thread


def readMsg(client_socket):
    global flag
    while flag:
        recv_data = client_socket.recv(1024)
        print('收到：', recv_data.decode('utf-8'))


def writeMsg(client_socket):
    global flag
    while flag:
        msg = input('>')
        msg = user_name + '说：' + msg
        client_socket.send(msg.encode('utf-8'))
        # 如果输入bye时候下线
        if msg.endswith('bye'):
            flag = False
            break



# 客户端
# 创建客户端套接字对象
client_socket = socket(AF_INET, SOCK_STREAM)

# 调用connect连接服务器
client_socket.connect(('192.168.1.4', 7878))
user_name = input('请输入用户名')
flag = True
# 开启一个线程处理客户端的读取消息
t = Thread(target=readMsg, args=(client_socket,))
t.start()
# 开启一个线程处理客户端的发送消息
t1 = Thread(target=writeMsg, args=(client_socket,))
t1.start()

t.join()
t1.join()

client_socket.close()
