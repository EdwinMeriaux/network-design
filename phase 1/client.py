import socket
import time
 
UDP_IP = "127.0.0.1"#IP address UDP is occuring at
UDP_PORT = 5005#port this program will output over
UDP_PORT2 = 5006#port from other socket
MESSAGE = b"Hello"

#settup to recieve from socket over port 5006
sock2 = socket.socket(socket.AF_INET, # Internet
                 socket.SOCK_DGRAM) # UDP
sock2.bind((UDP_IP, UDP_PORT2))

i = 0
while i < 2: ## loop to occure twice (recieve and send)
    print("start")
    sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print("sent")
    i = i + 1
    data, addr = sock2.recvfrom(1024) # buffer size of data
    print("received message: %s" % data)
    print("recieved")
    time.sleep(1)
print("done")