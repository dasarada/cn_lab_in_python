import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("192.168.43.13",2225))
while True:
        data,address=s.recvfrom(1024)
        print "server:"+str(data)
        input=raw_input("client:")
        if input=="bye" or input=="exit":
                s.sendto(input,("192.168.43.197",2225))
                s.close()
        else:
                s.sendto(input,("192.168.43.197",2225))
