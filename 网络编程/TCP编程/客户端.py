import socket

sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sk.connect(("www.sina.cn",80))

sk.send(b'GET / HTTP/1.1\r\nHost: www.sina.cn\r\nConnection: close\r\n\r\n')

data = []
while True:
    #每次接收1K的数据
    tempData = sk.recv(1024)
    if tempData:
        data.append(tempData)
    else:
        break

dataStr = (b''.join(data)).decode("utf-8")

sk.close()
# print(dataStr)

headers, HTML = dataStr.split('\r\n\r\n',1)
print(headers)
print(HTML)