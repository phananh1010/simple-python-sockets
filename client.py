## REFERENCE: https://stackoverflow.com/questions/15003778/i-want-to-stream-a-webcam-feed-using-socket-programming-in-python
##CLIENT

import socket
import time

host = "localhost"
port = 1890

for i in range(1):#send 1 package
    data = "hahaha".encode()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(data)
    s.close()
    time.sleep(0.5)