import socket #importing network library
import time #importing time library
 
UDP_IP = "127.0.0.1"#IP address UDP is occuring at
UDP_PORT = 5005#port this program will output over
UDP_PORT2 = 5006#port from other socket
MESSAGE = b"Hello"

#settup to recieve from socket over port 5006
sock2 = socket.socket(socket.AF_INET, # Internet
                 socket.SOCK_DGRAM) # UDP
sock2.bind((UDP_IP, UDP_PORT2))


print("output message:")
sock = socket.socket(socket.AF_INET, # Internet
                  socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
data, addr = sock2.recvfrom(1024) # buffer size of data
print("received echo: %s" % data)