import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'xujiatian',b'xuxiaomei',b'danping']:
    s.sendto(data,('127.0.0.1',9999))
    print(s.recv(1024).decode('utf-8'))
s.close()
