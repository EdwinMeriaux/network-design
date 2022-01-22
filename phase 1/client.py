import socket
import time
 
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
UDP_PORT2 = 5006
MESSAGE = b"Hello, World!"

sock2 = socket.socket(socket.AF_INET, # Internet
                 socket.SOCK_DGRAM) # UDP
sock2.bind((UDP_IP, UDP_PORT2))

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)
i = 0
while i < 2:
    print("start")
    sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print("sent")
    i = i + 1
    data, addr = sock2.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)
    print("recieved")
    time.sleep(1)
print("done")