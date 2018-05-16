import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(("192.168.0.117",8081))

server.listen(5)
# server.accept()
print("服务器启动")
clientSocket,clientAddress = server.accept()
print("%s--%s链接成功"%(str(clientSocket),clientAddress))
while True:
    data = clientSocket.recv(1024)
    # print("收到"+str(clientSocket)+"的数据："+data.decode("utf-8"))
    print("客户端说：" + data.decode("utf-8"))
    sendData = input("返回给客户端的数据")
    clientSocket.send(sendData.encode("utf-8"))