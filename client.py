import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.28.82", 5000))

while True:
    print(s.recv(1024).decode("utf-8"))