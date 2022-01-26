import socket

UDP_IP = "127.0.0.1" #IP address UDP is occuring at
UDP_PORT = 5005 #port from initial sender
UDP_PORT2 = 5006 #port this program will output over

#settup to recieve from socket over port 5005
sock = socket.socket(socket.AF_INET, # Internet
                 socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

i = 0
while i < 2: ## loop to occure twice (recieve and send)
     print("start")
     data, addr = sock.recvfrom(1024) # buffer size of data
     print("received message: %s" % data)
     print("recieved")
     sock2 = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
     sock2.sendto(data, (UDP_IP, UDP_PORT2))
     i = i + 1 #loop counter
     print("sent")
print("done")