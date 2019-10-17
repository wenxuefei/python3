from socket import *
import struct

filename = 'face.jpg'
server_id = '127.0.0.1'

# 封装读的请求
send_data = struct.pack('!H%dsb5sb' % len(filename), 1, filename.encode(), 0, 'octet'.encode(), 0)
# udp_socket套接字
udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.sendto(send_data, (server_id, 69))  # 读写端口默认为69

# 本地创建一个文件
f = open(filename, 'ab')  # a追加模式 b 二进制
while True:
    recv_data = udp_socket.recvfrom(1024)
    # print(recv_data)
    # 获取操作码及数据块编号
    caozuoma, ack_num = struct.unpack('!HH', recv_data[0][:4])
    # 判断操作码是否是5如果是5 则是错误信息
    if caozuoma == 5:
        print('文件不存在')
        break
    # 将接受到的数据写入文件中
    f.write(recv_data[0][4:])
    if len(recv_data[0]) < 516:  # 表示读取完毕
        break
    # 发送确认包
    ack_data = struct.pack('!HH', 4, ack_num)
    rand_port = recv_data[1][1]  # 获取服务器发送数据的随机端口
    udp_socket.sendto(ack_data, (server_id, rand_port))
