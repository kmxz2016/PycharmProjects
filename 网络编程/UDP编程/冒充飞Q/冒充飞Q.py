import socket
import time
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp.connect("192.168.0.117",2425)
udp.sendto("狂迷加油".encode("gbk"))
# while True:
#     udp.send("狂迷加油".encode("utf-8"))
#     time.sleep(1)