import socket

udpServer = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpServer.bind(('192.168.0.117',8900))

while True:
    data,addr = udpServer.recvfrom(1024)
    print("客户端说：",data.decode("utf-8"))
    info = input("返回给客户端的数据")
    udpServer.sendto(info.encode("utf-8"),addr)