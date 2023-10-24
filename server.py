## REFERENCE: https://stackoverflow.com/questions/15003778/i-want-to-stream-a-webcam-feed-using-socket-programming-in-python
##SERVER
import socket

host="localhost"
port=1890


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
while True:#always receive frames, never breaks
    conn, addr = s.accept()
    message = []
    while True:
        d = conn.recv(1024*1024)
        if not d: break
        else: message.append(d)
    data = '\n'.join(s.decode('utf-8', 'ignore') for s in message)
    print (f"received data: {data}")