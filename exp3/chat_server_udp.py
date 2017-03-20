import socket
udp_port=('192.168.43.197',2225)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(udp_port)
while True:
	input=raw_input("server: ")
	if input=="bye" or input=="exit":
		s.sendto(input,('192.168.43.13',2225))
		s.close()
	else:
		s.sendto(input,('192.168.43.13',2225))
	#print "hi"
	data,address=s.recvfrom(1024)
	#print "hi"
	print "client: "+str(data)
