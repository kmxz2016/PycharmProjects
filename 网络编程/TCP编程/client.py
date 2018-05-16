import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("192.168.0.117",8081))


# count = 0
while True:
    # count += 1
    data = input("请输入给服务器发送的数据")

    client.send(data.encode("utf-8"))
    info = client.recv(1024)
    print("服务器说：",info.decode("utf-8"))