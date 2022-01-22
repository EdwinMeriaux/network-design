import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
UDP_PORT2 = 5006

sock = socket.socket(socket.AF_INET, # Internet
                 socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

i = 0
while i < 2:
     data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
     print("received message: %s" % data)
     i = i + 1
     