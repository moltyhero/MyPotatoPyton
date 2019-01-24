# Message Receiver
import os
from socket import *


def main():
    host = ""
    port = 13000
    buf = 1024
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.bind(addr)
    print "Waiting to receive messages..."
    while True:
        (data, addr) = UDPSock.recvfrom(buf)
        print "Received message: " + data
        if data == "exit":
            break
    UDPSock.close()
    os._exit(0)


if __name__ == '__main__':
    main()